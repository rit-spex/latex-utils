@echo OFF
REM This is where you specify the path of your document.
set DOCUMENT_PATH="markdown_template.md"

REM This is where you specify the final name of your document.  Spaces will be replaced with underscores.
set FINAL_DOC_NAME="50_SAT"

REM You can specify the type of compiler script.  It expects an input of the path of the .tex document.
set COMPILE_SCRIPT="Compile_Scripts\\MikTexCompiler.bat"


REM Make sure you have python 3.X added to your path.
python markdown_compile.py %DOCUMENT_PATH% %COMPILE_SCRIPT% %FINAL_DOC_NAME%

pause