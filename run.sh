#!/bin/bash

python3 -m venv game-venv  # Check if python is installed
source game-venv/bin/activate  # Check if venv already exists
pip3 install -r requirements.txt
clear
python3 main.py