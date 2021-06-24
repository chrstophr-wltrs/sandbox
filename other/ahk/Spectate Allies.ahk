#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
; SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SendMode Event ; Only way to get AHK scripts working in LoL
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetKeyDelay, 35, 0
#UseHook, On; Also required for working LoL AHK scripts

keyArray := ["F3", "F2", "F5", "F4"]

keyInd := 0

#IfWinActive, ahk_exe League of Legends.exe 
{
    WheelUp::
    Send % "{" keyArray[keyInd] " up}"
    if (keyInd >= keyArray.Length()){
        keyInd := 1
    }
    else {
        keyInd ++
    }
    Send % "{" keyArray[keyInd] " down}"
    Return

    WheelDown::
    Send % "{" keyArray[keyInd] " up}"
    if (keyInd <= 1){
        keyInd := keyArray.Length()
    }
    else {
        keyInd --
    }
    Send % "{" keyArray[keyInd] " down}"
    Return

    Space::
    if (keyInd > 0){
        Send % "{" keyArray[keyInd] " up}"
    }
    Send {Space down}
    keyInd := 0
    Return

    Space Up::
    Send {Space up}
    Return
}

F11::Reload