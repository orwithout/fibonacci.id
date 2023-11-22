
@echo off
CALL %USERPROFILE%\miniconda3\Scripts\activate.bat senseurl

uvicorn main.main:app --reload --host 127.0.0.1 --port 8002 --log-level debug

pause


:: 
::@echo off
::wt.exe  "%~dp0start.cmd"
::START wt -d "D:\agent\sensevine" "D:\agent\sensevine\start.cmd"