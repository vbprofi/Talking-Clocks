@echo off
pyinstaller.exe --hidden-import="pyaudio, wave, sys, time, PyQt5" --add-data "wave/;./wave/" -w talking_clock.py
pause