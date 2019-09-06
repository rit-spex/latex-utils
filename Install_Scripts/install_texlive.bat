REM download install-tl.zip and unzip it
POWERSHELL -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest http://mirror.ctan.org/systems/texlive/tlnet/install-tl.zip -OutFile install-tl.zip"
POWERSHELL -Command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::ExtractToDirectory('install-tl.zip', '.'); }"
DEL install-tl.zip

REM an automated installation of TeXLive (infrastructure only)
CD install-tl-*
@ECHO | install-tl-windows.bat -no-gui
