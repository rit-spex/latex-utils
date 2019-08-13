#!/bin/bash
echo "Preparing to install Tectonic with Conda"
conda config --add channels conda-forge

echo "Installing Tectonic with Conda"
conda install tectonic
