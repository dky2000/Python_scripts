import uiautomator2 as ui2
import subprocess
import time
import os

# Connect to the target device (replace '192.168.2.57:5555' with your device's serial)
receiver_device_serial = "0123456789ABCDEF"
receiver_device = ui2.connect(receiver_device_serial)

def execute_adb(command):
    #subprocess.call(command, shell=True)
    os.system(command)

def open_google_play():
    execute_adb("adb shell am start -n com.android.vending/com.google.android.finsky.activities.MainActivity")
    time.sleep(3)

def adbUp():
    open_google_play()
    
    # 1. Instagram
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.instagram.android'")
    print("1. Instagram")
    time.sleep(5)
    receiver_device(description="Install").click()
    time.sleep(2)
    
    # 2. WhatsApp
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.whatsapp'")
    time.sleep(5)
    receiver_device(description="Install").click()
    time.sleep(2)
    
    # 3. Candy Crush
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.king.candycrushsaga'")
    time.sleep(5)
    receiver_device(description="Install").click()
    time.sleep(2)
    
    # 4. Truecaller
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.truecaller'")
    time.sleep(5)
    receiver_device(description="Install").click()
    time.sleep(2)
    
    # 5. OLX
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.olx.southasia'")
    time.sleep(5)
    receiver_device(description="Install").click()
    time.sleep(2)
adbUp()    

#if __name__ == "__main":
#    adbUp()
