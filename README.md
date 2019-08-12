# RIT-SPEX/latex-utils
This repository contains scripts for installing LaTeX configurations and to
compile TeX into beautiful documents.

# Install a LaTeX compiler on your machine
Use the following instructions to install a LaTeX compiler on your local machine.
On a Windows machine execute the commands in Powershell, else run them in Bash.

## Tectonic
Tectonic is a modern TeX distribution that has detailed error and status messages
and downloads packages on the fly. Tectonic is installed using 
[Anaconda/Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#), which works across most platforms including Windows, Mac, and Linux.

|     |     |
| --- | --- |
| **Windows** | `./install_scripts/install_tectonic_conda.bat` |
| **Mac/Linux** | `./install_scripts/install_tectonic_conda.sh` |

## MikTeX
MikTeX is a fully featured and stable inistallation used by many Windows users.
It downloads and installs packages as they are needed so the initial installation
is small and grows as you use more packages.

|     |     |
| --- | --- |
| **Windows** | `./install_scripts/install_miktex_win64.bat` |
| **Linux** | `./install_scripts/install_miktex_linux.sh` |

## MacTeX
MacTeX is a distribution of [TeX Live](https://www.tug.org/texlive/acquire-netinstall.html)
that is modified specifically for MacOS. TeX Live (and therefore MacTeX) do not
dynamically download packages. If you need to use a package that is not installed,
you must install it using the included GUI package manager.

|     |     |
| --- | --- |
| **Mac** | `./install_scripts/install_mactex.sh` |

# Use a Docker container instead
Rather than installing and managing a TeX distribution on your local machine,
you may prefer to send your TeX project to a Docker container for compilation.

First [install Docker](https://docs.docker.com/install/). Docker uses magic to
run virtual environments on your machine's turbo encabulators.

Compile a TeX project with Tectonic with a docker container with
```shell
./compile_scripts/compile_with_tectonic.sh
```