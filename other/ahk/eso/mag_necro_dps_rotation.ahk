#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%/pics  ; Ensures a consistent starting directory.
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

check(image_name = ""){
    global shades
    ImageSearch, image_x, image_y, 0, 0, A_ScreenWidth, A_ScreenHeight, % "*" shades " " image_name
    Return (ErrorLevel == 0)
}

swap(){
    Send -
    Sleep 1000
}

activate_ability(key_to_press = 0){
    Send %key_to_press%
}

weave(key_to_press = 0){
    Click
    activate_ability(key_to_press)
}

mage(pre_buff = false){
    if (!check("mage_icon.png") or check("mage_icon_1.png") or check("mage_icon_0.png")){
        if (!check("mage.png")){
            swap()
        }
        if (pre_buff){
            activate_ability(4)
        }
        else {
            weave(4)
        }
        Return True
    }
    Return false
}

minor_force(pre_buff = false){
    if (!check("force_icon.png") or check("force_icon_1.png") or check("force_icon_0.png")){
        if (!check("trap.png")){
            swap()
        }
        if (pre_buff){
            activate_ability(3)
        }
        else {
            weave(3)
        }
        Return True
    }
    Return false
}

degen(){
    if (!check("degen_icon.png") or check("degen_icon_1.png") or check("degen_icon_0.png")){
        if (!check("degen.png")){
            swap()
        }
        weave(2)
        Return True
    }
    Return false
}

blastbones(pre_buff = false){
    if (!(check("blastbones_ready.png") or check("blastbones_disabled.png"))){
        swap()
    }
    wait_for("blastbones_ready.png")
    if (pre_buff){
        activate_ability(4)
    }
    else {
        weave(4)
    }
}

siphon(){
    if (!check("siphon_icon.png") or check("siphon_icon_1.png") or check("siphon_icon_0.png")){
        if (!check("siphon_ready.png")){
            swap()
        }
        weave(3)
        Return True
    }
    Return false
}

mystic_orb(){
    if (!check("mystic_orb.png")){
        swap()
    }
    weave(2)
}

wall(){
    if (!check("unstable_wall.png")){
        swap()
    }
    weave(1)
}

boneyard(){
    if (!check("boneyard.png")){
        swap()
    }
    weave(1)
    Click
}

goliath(){
    if (check("goliath_ready.png")){
        weave("R")
    }
}

#UseHook, On
; 1::activate_ability("", 1)
; 2::activate_ability("", 2)
; 3::activate_ability("", 3)
; 4::activate_ability("", 4)
; 5::activate_ability("", 5)

F11::Reload  ; Ctrl+Alt+R
