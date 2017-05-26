Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\Users\marcos\Documents\Subversion\mirepo\python\socket-multi\iniciar_servidor.bat" & Chr(34), 0
Set WinScriptHost = Nothing

