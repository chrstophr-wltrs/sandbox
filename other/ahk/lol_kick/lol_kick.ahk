#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#Persistent

SetTimer, kick_me_from_league, 300

kick_me_from_league() {
    if (!WinExist("ahk_exe League of Legends.exe") and WinActive("ahk_exe LeagueClientUx.exe")) {
        ImageSearch, i_x, i_y, 0, 0, A_ScreenWidth, A_ScreenHeight, advanced_details.png
        if (ErrorLevel = 0) {
            WinClose
            MsgBox, Go work on some homework. 🙂
        }
    }
    Return
}