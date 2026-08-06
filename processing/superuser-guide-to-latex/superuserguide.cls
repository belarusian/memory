% superuserguide.cls
% Shared document class for the "Superuser Guide" series.
% Per Chapter 16: enforces required front-matter fields at the class level
% and centralizes the series' typographic conventions in one place.

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{superuserguide}[2026/01/01 v0.1 Superuser Guide series class]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions\relax
\LoadClass[11pt]{book}

% --- Fonts: LuaLaTeX + TeX Gyre Pagella, per the series' stated conventions ---
\RequirePackage{fontspec}
\setmainfont{TeX Gyre Pagella}

% --- Core packages used throughout the book ---
\RequirePackage[margin=1.25in]{geometry}
\RequirePackage{mathtools}
\RequirePackage{amsthm}
\RequirePackage{microtype}
\RequirePackage[colorlinks=true,linkcolor=black,citecolor=black,urlcolor=black]{hyperref}
\RequirePackage{tikz-cd}
\RequirePackage{makeidx}
\makeindex

% --- Shared theorem-like environments (Chapter 11) ---
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

% --- Required front-matter fields, enforced at class level (Chapter 16) ---
\newcommand{\bookauthor}[1]{\def\@bookauthor{#1}}
\newcommand{\bookaffiliation}[1]{\def\@bookaffiliation{#1}}
\newcommand{\bookdate}[1]{\def\@bookdate{#1}}
\def\@bookauthor{}
\def\@bookaffiliation{}
\def\@bookdate{}

\newcommand{\makebooktitle}{%
  \ifx\@title\@empty
    \ClassError{superuserguide}{A title is required: use \string\title{...} before \string\makebooktitle}{}
  \fi
  \ifx\@bookauthor\@empty
    \ClassError{superuserguide}{An author is required: use \string\bookauthor{...} before \string\makebooktitle}{}
  \fi
  \begin{titlepage}
    \centering
    \vspace*{3cm}
    {\Huge\bfseries \@title \par}
    \vspace{2cm}
    {\Large \@bookauthor \par}
    \ifx\@bookaffiliation\@empty\else
      \vspace{0.25cm}
      {\itshape \@bookaffiliation \par}
    \fi
    \vfill
    \ifx\@bookdate\@empty\else
      {\large \@bookdate \par}
    \fi
  \end{titlepage}
}

\endinput
