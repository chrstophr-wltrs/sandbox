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
global bar_swap_duration := 1000

wait_for(image_name = ""){ ; Waits for an image to be present on screen, loops until the image appears
    global shades
    loop {
        ImageSearch, image_x, image_y, 0, 0, A_ScreenWidth, A_ScreenHeight, % "*" shades " " image_name
        Sleep 50
    } until ErrorLevel = 0
}

swap(){
    Send -
    Sleep 1000
}

activate_ability(image_name = "", key_to_press = 0){
    Click
    Send %key_to_press%
    Return
}

#UseHook, On
; 1::activate_ability("unstable_wall.png", 1)
; 2::activate_ability("", 2)
; 3::activate_ability("", 3)
; 4::activate_ability("", 4)
; 5::activate_ability("", 5)

F11::Reload  ; Ctrl+Alt+R
