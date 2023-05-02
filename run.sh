#!/bin/bash

pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install aiogram

python3 src/telegram_ui.py
