@echo off
echo Setting up shapefile for Zilzila Bot
echo ====================================

REM Navigate to bot directory
cd /d "C:\Users\abdul\OneDrive\Рабочий стол\zilzilabot python"

REM Create directory
mkdir DATA\U 2>nul

REM Copy files
copy "C:\Users\abdul\OneDrive\Рабочий стол\ObHavoBot\bin\Debug\net8.0\Data\U\Umumiy osr smr\Export_Output_9.*" "DATA\U\"

echo.
echo Files in DATA\U:
dir DATA\U

echo.
echo Don't forget to update config.py with the correct path!
pause