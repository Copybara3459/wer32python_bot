@echo off

call %~dp0tele_bot\venv\Scripts\activate

cd %~dp0tele_bot

set BOT_TOKEN=5912081133:AAG7TU203xdM-BT5MfpYMnpr8f7x0iwcaCE

set PAYMENTS_TOKEN=1744374395:TEST:2f915e9e39cf6884d934

python bot_telegram.py

pause

