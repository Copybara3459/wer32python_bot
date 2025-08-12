@echo off

call %~dp0tele_bot\venv\Scripts\activate

cd %~dp0tele_bot

set BOT_TOKEN=N:A-A

set PAYMENTS_TOKEN=N:Name:an

python bot_telegram.py

pause


