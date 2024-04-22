import subprocess
import time
import os
import csv
total = 0
#number = int(input('Enter a number: '))
#n = int(input(""))
#if n == 1:
#   os.system('cls')
print("Test The internet connectivity")
time.sleep(2)
def execute_adb(command):
    subprocess.call(command, shell=True)
def check_internet():
    #execute_adb('adb shell /system/bin/ping -c 1 www.google.com -w 4 > clear')
    #cmd = execute_adb('adb shell /system/bin/ping -c 1 www.google.com > clear ')
    cmd = os.system('adb shell /system/bin/ping -c 1 www.google.com > clear')
    #os.system('adb shell clear')
    #os.system('cls')
    if cmd == 0:
        print('Internet is connected')
        rows = [['Internet is connected']]
    else:
        print('Internet is not connected')
        rows = [['Internet is not connected']]
    field = ['Result']
    filename = "test.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(field)
        csvwriter.writerows(rows)


if __name__ == '__main__':
    check_internet()