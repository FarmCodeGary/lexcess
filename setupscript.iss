; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{95394270-ED84-46A1-9235-3A74969BD228}
AppName=Lexcess
AppVerName=Lexcess 0.9
AppPublisher=Garrison Benson
AppPublisherURL=http://www.bensonbasement.com/games/lexcess/
AppSupportURL=http://www.bensonbasement.com/games/lexcess/
AppUpdatesURL=http://www.bensonbasement.com/games/lexcess/
DefaultDirName={pf}\Lexcess
DefaultGroupName=Lexcess
AllowNoIcons=yes
LicenseFile=C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\gpl.txt
OutputBaseFilename=Lexcess 0.9 Setup
SetupIconFile=C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\lexcessicon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\Lexcess.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\_tkinter.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\about.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\buzzer.wav"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\ding.wav"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\gameover.wav"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\gpl.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\help.html"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\hightone.wav"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\Lexcess.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\lexcessicon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\lowtone.wav"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\MSVCR71.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\python25.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\screenshot.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\tcl84.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\tk84.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\w9xpopen.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\winsound.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\wordset.dat"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Documents and Settings\Owner\workspace\Lexcess\src\dist\tcl\*"; DestDir: "{app}\tcl\"; Flags: ignoreversion recursesubdirs createallsubdirs

; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Lexcess"; Filename: "{app}\Lexcess.exe"; WorkingDir: "{app}"
Name: "{group}\Lexcess Website"; Filename: "http://www.bensonbasement.com/games/lexcess/"
Name: "{group}\{cm:UninstallProgram,Lexcess}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\Lexcess"; Filename: "{app}\Lexcess.exe"; WorkingDir: "{app}"; Tasks: desktopicon

[Run]
Filename: "{app}\Lexcess.exe"; WorkingDir: "{app}"; Description: "{cm:LaunchProgram,Lexcess}"; Flags: nowait postinstall skipifsilent

