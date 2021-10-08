#NoEnv
SetWorkingDir %A_ScriptDir%
CoordMode, Mouse, Window ;*[FGO Rerolling]
;SendMode Play
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetControlDelay 1
SetWinDelay 0
SetKeyDelay 50
SetMouseDelay -2
SetBatchLines -1

wait_for(image_name = ""){ ; Waits for an image to be present on screen, loops until the image appears
    global shades
    loop {
        ImageSearch, image_x, image_y, 0, 0, A_ScreenWidth, A_ScreenHeight, % "*" shades " " image_name
        Sleep 50
    } until ErrorLevel = 0
}