import re, glob, os
from math_lines import MATH_LINES
from inline_math import mathify_inline, restore_placeholders

SPECIAL = [
    ('\\', r'\textbackslash{}'),
    ('&', r'\&'),
    ('%', r'\%'),
    ('$', r'\$'),
    ('#', r'\#'),
    ('_', r'\_'),
    ('{', r'\{'),
    ('}', r'\}'),
    ('~', r'\textasciitilde{}'),
    ('^', r'\textasciicircum{}'),
]

def escape(text):
    for ch, repl in SPECIAL:
        text = text.replace(ch, repl)
    return text

def convert_file(path, chnum):
    lines = open(path, encoding='utf-8').read().split('\n')
    out = []
    in_code = False
    code_buf = []
    in_raw = False
    title = None
    for line in lines:
        if line.strip().startswith('```latex'):
            in_raw = True
            continue
        if in_raw:
            if line.strip().startswith('```'):
                in_raw = False
            else:
                out.append(line)
            continue
        if line.strip().startswith('```'):
            if not in_code:
                in_code = True
                code_buf = []
            else:
                in_code = False
                out.append(r'\begin{Verbatim}[breaklines=true, breaksymbolleft={}, fontsize=\small]')
                out.extend(code_buf)
                out.append(r'\end{Verbatim}')
            continue
        if in_code:
            code_buf.append(line)
            continue
        m1 = re.match(r'^# (?:Chapter \d+|Appendix [A-F]): (.+)$', line)
        if m1:
            title = m1.group(1).strip()
            t_math, t_ph = mathify_inline(title)
            out.append(r'\chapter{' + restore_placeholders(escape(t_math), t_ph) + '}')
            continue
        m2 = re.match(r'^## (?:\d+\.\d+|[A-F]\.\d+)\s+(.+)$', line)
        if m2:
            sec_title = m2.group(1).strip()
            s_math, s_ph = mathify_inline(sec_title)
            out.append(r'\section{' + restore_placeholders(escape(s_math), s_ph) + '}')
            continue
        if line.strip() == '':
            out.append('')
            continue
        key = (chnum, line.strip())
        if key in MATH_LINES:
            out.append(MATH_LINES[key])
            continue
        mathified, placeholders = mathify_inline(line)
        escaped = escape(mathified)
        restored = restore_placeholders(escaped, placeholders)
        out.append(restored)
    return title, '\n'.join(out)

files = sorted(glob.glob('/mnt/user-data/outputs/chapter-*.md'),
               key=lambda f: int(re.search(r'chapter-(\d+)-', f).group(1)))

os.makedirs('chapters', exist_ok=True)
manifest = []
for f in files:
    num = int(re.search(r'chapter-(\d+)-', f).group(1))
    title, tex = convert_file(f, num)
    outpath = f'chapters/ch{num:02d}.tex'
    open(outpath, 'w', encoding='utf-8').write(tex)
    manifest.append((num, title))

print("Chapters converted:", len(manifest))

appendix_files = sorted(glob.glob('/mnt/user-data/outputs/appendix-*.md'))
apx_manifest = []
for f in appendix_files:
    m = re.search(r'appendix-([a-f])-', f)
    letter = m.group(1).upper()
    title, tex = convert_file(f, letter)
    outpath = f'chapters/apx{letter}.tex'
    open(outpath, 'w', encoding='utf-8').write(tex)
    apx_manifest.append((letter, title))
print("Appendices converted:", len(apx_manifest), apx_manifest)
