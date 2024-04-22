
import subprocess
import time
def execute_adb(command):
    subprocess.call(command, shell=True)

def adbUp():
    #1. Insagram
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.instagram.android'  ")
    print("1. Insagram")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #2. whatsApp
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.whatsapp' ")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #3. Candy Crush
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.king.candycrushsaga' ")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #4. Truecaller
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.truecaller' ")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #5. Olx
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.olx.southasia' ")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)

adbUp()