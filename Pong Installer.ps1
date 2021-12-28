if(!([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
 Start-Process -FilePath PowerShell.exe -Verb Runas -ArgumentList "-File `"$($MyInvocation.MyCommand.Path)`"  `"$($MyInvocation.MyCommand.UnboundArguments)`""
 Exit
}

cd $PSScriptRoot

echo Installed:

tar -zxvf "Pong Installer.tar.gz" -C $Env:Programfiles

$SourceFilePath = $Env:Programfiles + "\Pong\Pong.exe"
$ShortcutPath = [Environment]::GetFolderPath("Desktop") + "\Pong.lnk"

$WScriptObj = New-Object -ComObject ("WScript.Shell")

$shortcut = $WscriptObj.CreateShortcut($ShortcutPath)
$shortcut.TargetPath = $SourceFilePath
$Shortcut.WorkingDirectory = $Env:Programfiles + "\Pong"
$shortcut.Save()

echo "Installation Finished!"

PAUSE