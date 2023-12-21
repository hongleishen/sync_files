@echo off
set "source="I:\OneDrive - Office\410_python\40_c_debug\code\usb_source"
set "destination="I:\OneDrive - Office\410_python\40_c_debug\code\usb"

echo Copying contents from %source% to %destination% ...
if exist "%destination%" (
    echo Deleting folder: %destination%
    rmdir /s /q "%destination%"
    echo Folder deleted.


@xcopy "%source%\*" "%destination%\" /E /H /C /I /Y

pause