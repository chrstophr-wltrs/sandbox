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

+LButton::
{
    Click, Down
    Return
}

F11::Reload