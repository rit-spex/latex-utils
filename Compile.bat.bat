@echo OFF
REM This is where you specify the path of your document.
set DOCUMENT_PATH="markdown_template.md"

REM This is where you specify the final name of your document.  Spaces will be replaced with underscores.
set FINAL_DOC_NAME="50_SAT"

REM You can specify the type of compiler mode.  You can give it a portable script to run that expects a tex file so you can use whatever latex tool you want if you create .bat to go with it.
set COMPILE_MODE="DOCKER"

REM Feel free to add other compiler options that are appropriate.
IF %COMPILE_MODE% == "DOCKER" ( REM Use Phil's docker script.
    set COMPILE_SCRIPT="Compile_Scripts\\DockerCompiler.bat"
) ELSE ( REM Use another option.  I have mine set up for a portable MixTex install.
    set COMPILE_SCRIPT=""
)

REM Make sure you have python 3.X added to your path.
python markdown_compile.py %DOCUMENT_PATH% %COMPILE_SCRIPT% %FINAL_DOC_NAME%

pause