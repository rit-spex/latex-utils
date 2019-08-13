@echo off
set INSTALL_PATH="https://miktex.org/download/ctan/systems/win32/miktex/setup/windows-x64/miktexsetup-2.9.6942-x64.zip"

REM Invoke the install and the unzip.
powershell -command "Invoke-WebRequest -OutFile install.zip %INSTALL_PATH%"
powershell -command "Expand-Archive -Force install.zip install"

REM Change directory
cd install

REM Download MikTex and install
echo "Starting installation"
miktexsetup --package-set=basic download
echo "Please wait...  This may take a while.  It will let you know when the installation is complete."
miktexsetup install
echo "Done installing, please double check to make sure MikTex is installed."
pause