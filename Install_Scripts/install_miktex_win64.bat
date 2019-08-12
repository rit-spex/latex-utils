echo "Downloading MikTeX installer"
wget https://miktex.org/download/win/miktexsetup-x64.zip
unzip miktexsetup-x64.zip

echo "Starting MikTeX installation"
miktexsetup --package-set=basic download

echo "Please wait...  This may take a while."
miktexsetup install

echo "Done installing, please check if MikTeX is installed (texify --help)."
