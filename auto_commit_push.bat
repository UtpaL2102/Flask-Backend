@echo off
cd /d "E:\Skill Work\C++ DSA(Questions)"  REM Change directory to your local DSA folder
git add .
git commit -m "Auto-commit on %DATE% %TIME%"
git push origin main
exit
