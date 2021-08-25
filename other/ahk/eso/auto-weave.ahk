#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%/pics  ; Ensures a consistent starting directory.
CoordMode, Mouse, Window
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetKeyDelay, 100
#maxThreadsPerHotkey, 2

weave(key_to_press = 0, flag = True) {
    if ((WinActive("ahk_exe eso64.exe")) and flag){
        Click
        Send %key_to_press%
        Sleep 200
        Click
    }
    else {
        Send %key_to_press%
    }
}

#UseHook, On

1::weave(1)
2::weave(2)
3::weave(3)
4::weave(4)
5::weave(5)

^1::weave(1, false)
^2::weave(2, false)
^3::weave(3, false)
^4::weave(4, false)
^5::weave(5, false)

F11::Reload