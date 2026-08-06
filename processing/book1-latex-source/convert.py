import re
import sys

def escape_latex(text):
    """Escape LaTeX special characters in ordinary prose text.
    Must NOT be applied inside code blocks or inline code spans."""
    # Order matters: backslash first
    text = text.replace('\\', r'\textbackslash{}')
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('$', r'\$')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    text = text.replace('{', r'\{')
    text = text.replace('}', r'\}')
    text = text.replace('~', r'\textasciitilde{}')
    text = text.replace('^', r'\textasciicircum{}')
    return text

def protect_inline_code(text, store):
    """Pull out `inline code` spans before escaping, replace with placeholders."""
    def repl(m):
        idx = len(store)
        store.append(m.group(1))
        return f"@@INLINECODE{idx}@@"
    return re.sub(r'`([^`]+)`', repl, text)

def restore_inline_code(text, store):
    for i, code in enumerate(store):
        placeholder = f"@@INLINECODE{i}@@"
        escaped = escape_latex(code)
        text = text.replace(placeholder, r'\texttt{' + escaped + '}')
    return text

def convert_inline_formatting(text):
    """Handle **bold**, *italic*, and inline code on a line of prose,
    after LaTeX-escaping has already happened on the non-code parts."""
    store = []
    text = protect_inline_code(text, store)
    text = escape_latex(text)
    # bold **...**
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    # italic *...*
    text = re.sub(r'\*(.+?)\*', r'\\emph{\1}', text)
    text = restore_inline_code(text, store)
    return text

def convert_markdown_to_latex(md_text, is_prologue=False):
    lines = md_text.split('\n')
    out = []
    i = 0
    n = len(lines)
    first_heading_used = False
    in_code_block = False
    code_buffer = []

    while i < n:
        line = lines[i]

        # Code block fences
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_buffer = []
            else:
                in_code_block = False
                out.append(r'\begin{Verbatim}[fontsize=\small, frame=single, xleftmargin=1em, xrightmargin=1em]')
                out.extend(code_buffer)
                out.append(r'\end{Verbatim}')
            i += 1
            continue

        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        stripped = line.strip()

        # Chapter/Prologue title (# ...)
        if stripped.startswith('# '):
            title = stripped[2:].strip()
            is_prologue_title = title.lower().startswith('prologue')
            title = re.sub(r'^Chapter\s+\d+\s*(\(excerpt\))?\s*:?\s*', '', title)
            title = re.sub(r'^Prologue\s*:?\s*', '', title)
            title_escaped = convert_inline_formatting(title)
            if is_prologue_title:
                out.append(r'\chapter*{' + title_escaped + '}')
                out.append(r'\addcontentsline{toc}{chapter}{' + title_escaped + '}')
                out.append(r'\markboth{' + title_escaped + '}{' + title_escaped + '}')
            else:
                out.append(r'\chapter{' + title_escaped + '}')
            first_heading_used = True
            i += 1
            continue

        # Section (## ...)
        if stripped.startswith('## '):
            title = stripped[3:].strip()
            title_escaped = convert_inline_formatting(title)
            out.append(r'\section*{' + title_escaped + '}')
            i += 1
            continue

        # Blank line
        if stripped == '':
            out.append('')
            i += 1
            continue

        # Ordinary paragraph line
        out.append(convert_inline_formatting(line))
        i += 1

    return '\n'.join(out)


if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    with open(infile, 'r') as f:
        md = f.read()
    latex = convert_markdown_to_latex(md)
    with open(outfile, 'w') as f:
        f.write(latex)
    print(f"Converted {infile} -> {outfile}")
