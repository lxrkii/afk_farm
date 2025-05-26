#Persistent
#NoEnv
SendMode, Input
SetTitleMatchMode, 2

targetWindowTitle := "Notepad"
toggle := false

End::
toggle := !toggle

if (toggle) {
    SetTimer, SendKeysToWindow, 100
} else {
    SetTimer, SendKeysToWindow, Off
}
return

SendKeysToWindow:
if !WinExist(targetWindowTitle) {
    return
}

ControlSend,, w, %targetWindowTitle%
Sleep, 200
ControlSend,, a, %targetWindowTitle%
Sleep, 200
ControlSend,, s, %targetWindowTitle%
Sleep, 200
ControlSend,, d, %targetWindowTitle%
Sleep, 200
return
