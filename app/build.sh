#!/bin/bash
pyinstaller -F --onefile --add-data "./resources/truck.png:." --add-data "./resources/muruntau.png:." --hidden-import=tkinter --hidden-import=_tkinter -w run.py
