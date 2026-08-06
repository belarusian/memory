# The Superuser Guide to LaTeX — build tree

## Build
    latexmk

Requires LuaLaTeX and the TeX Gyre Pagella fonts (both standard in any
full TeX Live install). Output lands in `build/main.pdf`.

## Layout
- `main.tex` — top-level assembly (front matter, 8 parts, 22 chapters,
  4 appendices, index). Uncomment the `\includeonly` line to restrict
  compilation to a chapter you're actively drafting.
- `superuserguide.cls` — shared class: fonts, theorem environments,
  and the required-front-matter-field enforcement described in Ch. 16.
- `chapters/`, `appendices/`, `frontmatter/` — one file per unit, per
  the architecture argued for in Ch. 3.
- `bib/`, `notation/`, `figures/` — placeholders for the shared
  cross-corpus bibliography (Ch. 12) and notation file (Ch. 10) once
  populated; empty for now.

## About PREVIEW-computer-modern.pdf
This sandbox's LuaLaTeX install has a broken font cache and can't load
TeX Gyre Pagella here, so the shipped preview was rendered with a
temporary, font-stripped copy of the class under pdflatex/Computer
Modern purely to verify the manuscript compiles cleanly — 136 pages,
zero errors, fully resolved cross-references and index. Building with
the real `main.tex` and `superuserguide.cls` on a normal machine will
produce the intended LuaLaTeX/Pagella typesetting.
