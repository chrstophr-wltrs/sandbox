#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
CoordMode, Mouse, Window
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetKeyDelay, 35, 0

global shades := 0

wait_for(image_name = ""){ ; Waits for an image to be present on screen, loops until the image appears
    global shades
    loop {
        ImageSearch, image_x, image_y, 0, 0, A_ScreenWidth, A_ScreenHeight, % "*" shades " " image_name
        Sleep 50
    } until ErrorLevel = 0
}

F11::Reload  ; Ctrl+Alt+R
