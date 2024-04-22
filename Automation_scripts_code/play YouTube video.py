
import subprocess

import time
def execute_adb(command):
    subprocess.call(command, shell=True)
def adbUp():
    #execute_adb("adb shell input keyevent 26")
    if execute_adb()
    execute_adb("adb shell input swipe 10 1000 10 10")
    print("Youtube App Open")
    execute_adb("adb shell am start -a com.google.android.youtube.action.open.search -n com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity")
    time.sleep(5)
    #execute_adb("adb shell input keyevent 44 53 48 36 43 42 62 48 49 48 43 46 37 29 40")
    execute_adb('adb shell input text "Python%stutorial " ')
    time.sleep(2)
    execute_adb("adb shell input tap 260 250")
    time.sleep(2)
    execute_adb("adb shell input swipe 10 1000 10 10")
    time.sleep(1)
    execute_adb("adb shell input swipe 10 1000 10 10")
    time.sleep(2)
    execute_adb("adb shell input tap 260 250")
    timer=time.time()+1*60;
    print("Stop the Video")
    execute_adb("adb shell input keyevent 85")
    time.sleep(5)
    print("Run The Video")
    execute_adb("adb shell input keyevent 85")

adbUp()

"""

import subprocess

# Run the adb shell monkey command
monkey_command = "adb shell monkey -v --throttle 500 --ignore-crashes --monitor-native-crashes --ignore-timeouts --kill-process-after-error --ignore-security-exceptions -v 500"
subprocess.run(monkey_command, shell=True, check=True)

# Restart the Android device
restart_command = "adb reboot"
subprocess.run(restart_command, shell=True, check=True)

"""