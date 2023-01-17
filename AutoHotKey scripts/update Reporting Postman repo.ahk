#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
pgdn & pgup::
Send, sudo su {Enter}
Sleep, 2000
Send, u
Sleep, 50
Send, t
Sleep, 50
Send, e
Sleep, 50
Send, {Enter} 
Sleep, 2000
Send, cd /home/ute/Reporting_Portal_Postman {Enter}
Sleep, 500
Send, git stash {Enter}
Sleep, 2000
Send, git pull https://gitlabe2.ext.net.nokia.com/ksurowka/Reporting-Portal-Postman {Enter}
Sleep, 2000
Send, chmod 777 -R * {Enter}
Sleep, 500
Send, chown jenkins -R * {Enter} 
Sleep, 500
Send, chgrp jenkins -R * {Enter}
return