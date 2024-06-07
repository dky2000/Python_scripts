
import subprocess
import os
import time
from datetime import datetime
import csv
import threading

def execute_adb(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{command}': {e.output.decode('utf-8')}")
        return ""

def adbUp():
    screen_state = execute_adb('adb shell "dumpsys input_method | grep screenOn"')
    print("Screen state output:", screen_state)

    if "screenOn = false" in screen_state:
        print("Screen is off. Executing commands...")
        execute_adb("adb shell input keyevent 26")
        time.sleep(2)

    execute_adb("adb shell input swipe 10 1000 10 10")
    time.sleep(2)
    execute_adb("adb shell input keyevent KEYCODE_APP_SWITCH")
    time.sleep(2)
    execute_adb("adb shell input tap 174 1450")
    time.sleep(2)
    print("WhatsApp Open")
    execute_adb("adb logcat -c")
    execute_adb("adb logcat -c")
    t = threading.Thread(target=execute_adb, args=('adb logcat > dh.txt',))
    t.start()
    execute_adb("adb shell am start -n com.whatsapp/.Main")
    time.sleep(5)
    execute_adb("adb shell input tap 602 1415")
    time.sleep(3)

def write_to_csv(call_start_time, call_end_time, call_number):
    # Check if the file exists to determine whether to write the headers
    file_exists = os.path.isfile('call_times.csv')

    with open('call_times.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write column headers if the file doesn't exist
        if not file_exists:
            writer.writerow(["Sr. No", "Call Start Time", "Call End Time"])

        writer.writerow([call_number, call_start_time, call_end_time])

adbUp()

for i in range(1, 2):
    print(i)
    execute_adb("adb shell input tap 650 415")
    start_time = datetime.now().strftime("%H:%M:%S")
    print("Call Start Time")
    print(start_time)
    time.sleep(10)

    execute_adb("adb shell input tap 606 1385")
    end_time = datetime.now().strftime("%H:%M:%S")
    print("Call end Time")
    print(end_time)

    write_to_csv(start_time, end_time, i)

execute_adb("adb shell killall -2 logcat > clr")

# Define write_to_txt function outside of the write_to_csv function
"""
def write_to_txt():
    # Read the data from the text file
    with open("rssi_value_1.txt", "rb") as file:
        lines = file.readlines()

    # Extract lines containing "rssi" and print them
    for line in lines:
        dec_line = line.decode("utf-8", errors='ignore')
        #dec_line = line.decode("utf-8", errors='ignore')
        if "rssi" in dec_line:
            # print(dec_line)
            rssi_value = dec_line.split("rssi: ")
            if len(rssi_value) == 2:
                print("rssi:", rssi_value[1].strip())

    # Call the write_to_txt function
write_to_txt()
"""
