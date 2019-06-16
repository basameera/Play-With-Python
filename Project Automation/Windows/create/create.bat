@echo off
set projectName=%1
IF "%projectName%"=="" (
    echo Error: Need Project Name as argument
    REM exit
)
echo run
:: echo face-cmd -u %arg1% -p %arg2%