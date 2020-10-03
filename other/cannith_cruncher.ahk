#NoEnv
SetWorkingDir %A_ScriptDir%
CoordMode, Mouse, Window ;*[FGO Rerolling]
;SendMode Play
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetControlDelay 1
SetWinDelay 0
SetKeyDelay 500
SetMouseDelay -2
SetBatchLines -1

 global shades := 0

wait_for(image_name = ""){ ; Waits for an image to be present on screen, loops until the image appears
    global shades
    loop {
        ImageSearch, image_x, image_y, 0, 0, A_ScreenWidth, A_ScreenHeight, % "*" shades " " image_name
        Sleep 50
    } until ErrorLevel = 0
}

click_on(image_name, x_adjust := 0, y_adjust := 0){ ; Waits for an image, then moves to it and clicks it
    global shades
    wait_for(image_name)
    ImageSearch, image_x, image_y, 0, 0, A_ScreenWidth, A_ScreenHeight, % "*" shades " " image_name
    image_x := image_x + x_adjust
    image_y := image_y + y_adjust
    Click, %image_x%, %image_y%, Left, 1
}

click_drag(image_name, x_adjust := 0, y_adjust := 0){ ; Waits for an image, then clicks and drags from the current location to the image's location
    global shades
    wait_for(image_name)
    ImageSearch, image_x, image_y, 0, 0, A_ScreenWidth, A_ScreenHeight, % "*" shades " " image_name
    image_x += x_adjust
    image_y += y_adjust
    Click Down 
    Sleep 50
    MouseMove, %image_x%, %image_y%, 5
    Sleep 50
    Click Up
}

deconstruct(){
    MouseGetPos, home_x, home_y
    click_drag("clear.png", , -15)
    click_on("dissolve.png")
    click_on("deconstruct.png")
    MouseMove, %home_x%, %home_y%
}

move_bank(){
    MouseGetPos, home_x, home_y
    click_drag("bank.png", -150, 150)
    MouseMove, %home_x%, %home_y%
}

+LButton::
{
    (ImageSearch, , , 0, 0, A_ScreenWidth, A_ScreenHeight, % "*" shades " cannith.png")
    if (ErrorLevel = 0){
        deconstruct()
        Return
    }
    (ImageSearch, , , 0, 0, A_ScreenWidth, A_ScreenHeight, % "*" shades " bank.png")
    if (ErrorLevel = 0){
        move_bank()
        Return
    }
    else{
        Send, +{LButton}
        Return
    }
}

F11::Reload