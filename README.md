# RIT-SPEX/latex-utils
This repository contains scripts for turning TeX into beautiful documents.

## Table of Contents
* [Prerequisite Software](#prerequisite-software)
* [Install a LaTeX compiler on your machine](#Install-a-LaTeX-compiler-on-your-machine)
    * [Tectonic](#Tectonic)
    * [MikTeX](#MikTeX)
    * [TeX Live](#TeX-Live)
    * [Use a Docker container instead](#Use-a-Docker-container-instead)
* [Compiling Markdown to LaTeX with a Template](#Compiling-Markdown-to-LaTeX-with-a-Template)
    * [Supported syntax](#Supported-syntax)
        * [Special tags](#Special-tags)
        * [Comments](#Comments)
    * [Run the Markdown-to-TeX compiler](#Run-the-Markdown-to-TeX-compiler)


# Prerequisite Software
These tools assume the user has the following software installed on their
machine. Installation and usage instructions will not cover using this
software.

* Python 3.x
* (Mac only)
  [Homebrew](https://treehouse.github.io/installation-guides/mac/homebrew)
* (Optional) Docker Desktop

**Note:** Documentation for this repository assumes that a Windows user is
using Windows Powershell. While most of the Linux instructions should work
within the Windows Subsystem for Linux (WSL) environment on a Windows machine,
proceed at your own risk.

# Install a LaTeX compiler on your machine
Use the following instructions to install a LaTeX compiler on your local
machine. On a Windows machine execute the commands in Powershell, else run them
in Bash.

## Tectonic
Tectonic is a modern TeX distribution that has detailed error and status
messages and downloads packages on the fly. Tectonic is installed using
[Anaconda/Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#),
which works across most platforms including Windows, Mac, and Linux.

|     |     |
| --- | --- |
| **Windows** | `./install_scripts/install_tectonic_conda.bat` |
| **Mac/Linux** | `./install_scripts/install_tectonic_conda.sh` |

## MikTeX
MikTeX is a fully featured and stable inistallation used by many Windows users.
It downloads and installs packages as they are needed so the initial
installation is small and grows as you use more packages.

|     |     |
| --- | --- |
| **Windows** | `./install_scripts/install_miktex_win64.bat` |
| **Linux** | `apt-get install miktex` |

## TeX Live
TeX Live is the "standard" TeX distribution. MacTeX is a distribution of TeX
Live that is modified specifically for MacOS. TeX Live (and MacTeX) do not
dynamically download packages. If you need to use a package that is not
installed, you must install it using the included GUI package manager.

|     |     |
| --- | --- |
| **Windows** | `` |
| **Mac** | `brew cask install mactex` |
| **Linux** | `apt-get install texlive` |

## Use a Docker container instead
Rather than installing and managing a TeX distribution on your local machine,
you may prefer to send your TeX project to a Docker container for compilation.

First [install Docker](https://docs.docker.com/install/). Docker uses magic to
run virtual environments on your machine's turbo encabulators.

Compile a TeX project with Tectonic with a docker container with
```shell
./compile_scripts/compile_with_tectonic.sh
```

# Compile Markdown to TeX with a Template
The Python script `Portable_PDD/markdown_compile.py` is used to convert a
Markdown (`.md`) text file into a LaTeX (`.tex`) file following a given TeX
template. This script also allows mixed Markdown and TeX formatting in the same
file.

The Markdown to LaTeX compiler makes writing content faster, easier, and more
readable by beginning in Markdown and formatting to TeX automatically. A TeX
template is used to format the resultant `.tex` file, including titles, author
blocks, section formatting, and so on.

## Supported syntax
| Syntax | Markdown | LaTeX |
| ------ | -------- | ----- |
| Sections | `# my section` | `\section{my section}` |
| Subsections | `## my subsection` | `\subsection{my subsection}` |
| Paragraph text | as is | as is |
| Line breaks | (empty line between paragraphs) | (empty line between paragraphs) |
| Basic LaTeX syntax | typed as normal text | as is |

### Special tags
The `.tex` template defines the names of special tags and dictates where they
are used. At very start of the Markdown file, define tags and their values. The
values are injected directly into the `.tex` template exactly as they are
entered here.

```markdown
---
TITLE_TAG: 50\$ Satellite PDD
AUTHORS_TAG: Evan Putnam, Another Student
EMAIL_TAG: emp9173@rit.edu, someOtherEmail@spex.com
TEMP_TAG: Hello World
---
```

### Comments
Comments are allowed in the Markdown file, but they are ignored by the compiler
will not appear in the resultant TeX file.

There can only be one single line comment per line. Nested comments are not
supported. Multiline comments are only supported if you have a single start and
end on a separate line.

```
<!---
this
is
allowed
--->
```
```
<!--- this
is
not --->
```

## Run the Markdown-to-TeX compiler
instructions on how to actually run the compiler
