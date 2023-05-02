#!/bin/bash

pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install matplotlib

python3 main.py
