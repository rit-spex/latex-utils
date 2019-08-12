echo "Starting installation"
miktexsetup --package-set=basic download
echo "Please wait...  This may take a while.  It will let you know when the installation is complete."
miktexsetup install
echo "Done installing, please double check to make sure MikTex is installed."
pause