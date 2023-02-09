; #NoEnv ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


F8:: Run, C:\ENG_APPS\Python\pythonw.exe C:\Users\KS5752\PycharmProjects\personal-quick-actions\main.py;
F8 & 0:: Send, 💀
F8 & 9:: Send, 👉👈
F8 & 8:: Send, 🥹  ;
F8 & 7:: Send, 🥺
; ^Insert:: Send % regexReplace(clipboard, "\R{2,}", "`n");