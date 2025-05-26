#Persistent
#NoEnv
SetBatchLines, -1
SendMode, Input

toggle := false  ; флаг вкл/выкл
loopActive := false

End::
toggle := !toggle
if (toggle && !loopActive) {
    loopActive := true
    SetTimer, LoopWASD, 10
} else if (!toggle && loopActive) {
    SetTimer, LoopWASD, Off
    loopActive := false
}
return

LoopWASD:
SetTimer, LoopWASD, Off  ; Отключаем таймер, чтобы избежать одновременного выполнения

Loop {
    if (!toggle) {
        break
    }

    Send, w
    Sleep, 200
    Send, a
    Sleep, 200
    Send, s
    Sleep, 200
    Send, d
    Sleep, 200
}
SetTimer, LoopWASD, On
return
