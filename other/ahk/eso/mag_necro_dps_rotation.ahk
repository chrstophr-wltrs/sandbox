#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%/pics  ; Ensures a consistent starting directory.
CoordMode, Mouse, Window
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetKeyDelay, 200
#maxThreadsPerHotkey, 2

toggle := false
global shades := 50

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

blastbones(pre_buff = false){
    ; weave cooldown: 1000 ms
    if (check("blastbones_disabled.png")){
        wait_for("blastbones_ready.png")
    }
    if (pre_buff){
        activate_ability(4)
    }
    else {
        weave(4)
    }
}

boneyard(){
    weave(1)
    Sleep 100
    Click
}

degen(){
    if (check("degen_dim.png")){
        wait_for("degen.png")
    }
    weave(2)
    Return True
}

goliath(){
    if (check("goliath_ready.png")){
        weave("R")
        Sleep 100
        Click
        Sleep 1000
    }
}

mage(pre_buff = false){
    ; weave cooldown: 1000 ms
    if (pre_buff){
        activate_ability(4)
    }
    else {
        weave(4)
    }
}

minor_force(pre_buff = false){
    if (pre_buff){
        activate_ability(3)
    }
    else {
        weave(3)
    }
    Sleep 100
    Click
}

mystic_orb(pre_buff = false){
    if (pre_buff){
        activate_ability(2)
    }
    else {
        weave(2)
    }
}

rune(){
    ; weave cooldown: 700
    weave(5)
    Sleep 100
    Click
}

siphon(){
    ; weave cooldown: 1000
    if (check("siphon_dim.png")){
        wait_for("siphon_ready.png")
    }
    weave(3)
}

wall(){
    weave(1)
}

static_rotation(toggle){
    if (WinActive("ahk_exe eso64.exe")){
        ; toggle = !toggle
        ; while (toggle) {
            blastbones()
            swap()
            boneyard()
            wall()
            swap()
            blastbones()
            siphon()
            swap()
            mystic_orb()
            ; swap()
            ; blastbones()
            ; minor_force()
            ; rune()
            ; swap()
            ; blastbones()
            ; degen()
            ; mage()
        ; }
    }
}

experimental_rotation(toggle){
    if (WinActive("ahk_exe eso64.exe")){
    ; toggle = !toggle
    ; while (toggle) {
        blastbones()
        Sleep 1000
        siphon()
        swap()
        wall()
        swap()
        blastbones()
        Sleep 1000
        boneyard()
        swap()
        rune()
        swap()
        blastbones()
        Sleep 1000
        degen()
        swap()
        mage()
        swap()
        blastbones()
        swap()
        mystic_orb()
        Sleep 1000
        minor_force()
        swap()
        goliath()
    ; }
}
Return
}

flex(){
    if (!(goliath() or mage() or minor_force() siphon() or degen())){
        rune()
    }
}

dynamic_rotation(toggle){
    if (WinActive("ahk_exe eso64.exe")){
        ; toggle = !toggle
        ; while (toggle) {
            wall()
            swap()
            blastbones()
            Sleep 1000
            boneyard()
            swap()
            Sleep 100
            mystic_orb()
            swap()
            ; Sleep 100
            blastbones()
            flex()
            Sleep 200
            flex()
            Sleep 200
            blastbones()
            ; flex()
        ; }
    }
}

pre_buff(){
    if (WinActive("ahk_exe eso64.exe")){
        mage(True)
        Sleep 700
        mystic_orb(True)
        swap()
        blastbones(True)
        Sleep 700
        goliath()
        swap()
        minor_force()
        swap()
    }
}

cooldown_testing(){
    if (WinActive("ahk_exe eso64.exe")){
        rune()
        swap()
        Sleep 1000
        weave(5)
    }
}

#UseHook, On
6::cooldown_testing()

7::pre_buff()

F11::Reload  ; Ctrl+Alt+R
