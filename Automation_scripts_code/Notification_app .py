import subprocess
import os
import time
import re

apps = {
    "Message": "com.google.android.apps.messaging/.ui.ConversationListActivity",
    "Instagram": "com.instagram.android/com.instagram.mainactivity.InstagramMainActivity",
    "Facebook": "com.facebook.katana/.LoginActivity",
    "WhatsApp": "com.whatsapp/.Main",
    "imo": "com.imo.android.imoim/.activities.Home",
    "Teams": "com.microsoft.teams/com.microsoft.skype.teams.Launcher",
    "Telegram": "org.telegram.messenger/.DefaultIcon",
    "Gmail": "com.google.android.gm/.ConversationListActivityGmail"
}

def open_app(app_name, package_name):
    #print(package_name)
    os.system(f'adb shell am start -n {package_name}')
    time.sleep(5)

print("Choose apps to open:")
for i, app in enumerate(apps):
    print(f"{i}. {app}")


choices = input("Enter the select apps : ")
app_choices = [int(choice) for choice in re.split(r'[,\s]+', choices) if choice.isdigit()]
print(app_choices)

########################################################################
def execute_adb(command):
    subprocess.call(command,shell=True)

########################################################################0
def Message():
    execute_adb('adb shell input tap 410 1344')
    time.sleep(1)
    execute_adb('adb shell input text "6392736654"')
    time.sleep(2)
    execute_adb('adb shell input keyevent 66')
    time.sleep(2)
    execute_adb('adb shell input text "Message%sTest1"')
    time.sleep(2)
    #execute_adb('adb shell input tap 606 880')
    time.sleep(2)


########################################################################1
def Instagram():
    execute_adb('adb shell input tap 608 48')
    time.sleep(2)
    execute_adb('adb shell input tap 176 670')
    time.sleep(2)
    execute_adb('adb shell input text "Test1"')
    time.sleep(2)
    #execute_adb('adb shell input tap 617 891')
    time.sleep(2)
########################################################################2

def Facebook():
    execute_adb('adb shell input tap 624 48')
    time.sleep(2)
    execute_adb('adb shell input tap 171 508')
    time.sleep(2)
    execute_adb('adb shell input text "Test1"')
    time.sleep(2)
    #execute_adb('adb shell input tap 617 891')
    time.sleep(2)


########################################################################3
def WhatsApp():
    execute_adb('adb shell input tap 144 296')
    time.sleep(2)
    execute_adb('adb shell input text "Test1"')
    time.sleep(2)
    #execute_adb('adb shell input tap 617 891')
    time.sleep(2)
#WhatsApp()

########################################################################4

def imo():
    execute_adb('adb shell input tap 648 1432')
    time.sleep(2)
    execute_adb('adb shell input text "Deepak"')
    time.sleep(2)
    execute_adb('adb shell input tap 134 261')
    time.sleep(2)
    execute_adb('adb shell input text "Test1"')
    time.sleep(2)
    #execute_adb('adb shell input tap 617 891')
    time.sleep(2)
########################################################################5

def Teams():
    execute_adb('adb shell input tap 158 374')
    time.sleep(2)
    execute_adb('adb shell input tap 88 1399')
    time.sleep(2)
    execute_adb('adb shell input text "Test1"')
    time.sleep(2)
    #execute_adb('adb shell input tap 632 887')
    time.sleep(2)
########################################################################6
def Telegram():
    execute_adb('adb shell input tap 624 48')
    time.sleep(2)
    execute_adb('adb shell input text "Deepak"')
    time.sleep(2)
    execute_adb('adb shell input tap 158 306')
    time.sleep(2)
    execute_adb('adb shell input text "Test1"')
    time.sleep(2)
    #execute_adb('adb shell input tap 624 898')
    time.sleep(2)


########################################################################7
def Gmail():
    execute_adb('adb shell input tap 403 1264')
    time.sleep(2)
    execute_adb('adb shell input text "lavaworkid@gmail.com"')
    time.sleep(2)
    execute_adb('adb shell input tap 144 514')
    time.sleep(2)

    execute_adb('adb shell input tap 429 748')
    time.sleep(2)
    execute_adb('adb shell input text "Test1"')
    time.sleep(2)
    #execute_adb('adb shell input tap 528 64')
    time.sleep(2)






########################################################################7
########################################################################7
########################################################################7
########################################################################7
########################################################################7

for choice in app_choices:
    if 0 <= choice < len(apps):
        selected_app = list(apps.keys())[choice]
        print(selected_app)
        package_name = apps[selected_app]
        print(f"Opening {selected_app}...")
        open_app(selected_app, package_name)
        time.sleep(3)
        if choice == 0:
            Message()
        elif choice == 1:
            Instagram()
        elif choice == 2:
            Facebook()
        elif choice == 3:
            WhatsApp()
        elif choice == 4:
            imo()
        elif choice == 5:
            Teams()
        elif choice == 6:
            Telegram()
        elif choice == 7:
            Gmail()



