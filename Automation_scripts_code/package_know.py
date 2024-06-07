#How to package name in all apps
import subprocess
import time
def execute_adb(commands):
    subprocess.call(commands, shell=True)

def adbUp():
    execute_adb("adb devices")
    execute_adb('adb shell "pm dump com.whatsapp">package_w.txt')
adbUp()
#lines = package_w.txt

with open('package_w.txt', 'r') as f:
    for line in f:
        if "cmp" and "baseIntent" in line:
            cmp_index= line.split("cmp=")
            component = cmp_index[1].replace("}", " ")
            print(component)



#activity name know cmd commands -> adb shell "dumpsys package com.whatsapp | grep  -A 2 MAIN"
#adb shell "dumpsys package com.whatsapp | grep  -A 2 LAUNCHER"
#adb shell "pm dump com.whatsapp">package_w.txt
#adb shell "pm dump com.whatsapp| grep -A 2 -i launcher"
#app open commands -> adb shell am start -S com.whatsapp/.Main