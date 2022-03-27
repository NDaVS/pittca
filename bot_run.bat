@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=ТУТ ТОКЕН БЕЗ КАВЫЧЕК

python main.py

pause