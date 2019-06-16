@echo off
echo *** Git-Bass ***
REM echo %~1

set commitMsg=%~1
IF "%commitMsg%"=="" (
    echo ERROR: Need Commit Message as argument
    exit /B
)
set dir=%cd%
REM echo %commitMsg%

:: check repo for pulls
git pull

:: get git remote url
FOR /F "tokens=* USEBACKQ" %%F IN (`git config --get remote.origin.url`) DO (
SET gitrepo=%%F
)
REM ECHO %gitrepo%

:: lets push
git status
git add .
git commit -m %commitMsg%
git push