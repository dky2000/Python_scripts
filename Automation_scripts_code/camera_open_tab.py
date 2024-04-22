import subprocess

import time
def execute_adb(command):
    subprocess.call(command, shell=True)
def adbUp():
    print("Camera App Open")
    execute_adb("adb shell am start -n com.android.camera/.CameraActivity")
    time.sleep(3)
    execute_adb("adb shell input tap 200 200")
    time.sleep(2)

adbUp()

def tap():
    for a in range(1, 50000):
        execute_adb("adb shell input tap 450 340")
        time.sleep(1)
        print(f'Loop: {a}')

tap()