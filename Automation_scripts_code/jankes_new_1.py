import os
import time
import re
import openpyxl

# workbook = openpyxl.Workbook()
#
# # Select the active sheet (the default first sheet)
# worksheet = workbook.active

# Dictionary of apps and their package names
apps = {
    "YouTube": "com.google.android.youtube/com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity",
    "Instagram": "com.instagram.android/com.instagram.mainactivity.InstagramMainActivity",
    "Facebook": "com.facebook.katana/.activity.FbMainTabActivity",
    "WhatsApp": "com.whatsapp/.Main"
}

# Function to open an app
def open_app(app_name, package_name):
    #print(package_name)
    os.system(f'adb shell am start -n {package_name}')
    time.sleep(5)

# Function to perform scrolling actions
def scroll():
    for a in range(1, 2):
        swipe_command = 'adb shell input touchscreen swipe 440 1380 440 280 200'
        os.system(swipe_command)
        time.sleep(5)
        print(f'loop: {a}')

# Print the list of apps with serial numbers
print("Choose apps to open:")
for i, app in enumerate(apps):
    print(f"{i}. {app}")

# Get user input for the selected apps
choices = input("Enter the serial numbers of the apps you want to open and scroll (comma or space-separated): ")
app_choices = [int(choice) for choice in re.split(r'[,\s]+', choices) if choice.isdigit()]

# Iterate through the selected apps, open them one by one, and collect graphics info
for choice in app_choices:
    if 0 <= choice < len(apps):
        selected_app = list(apps.keys())[choice]
        package_name = apps[selected_app]
        print(f"Opening {selected_app}...")
        open_app(selected_app, package_name)
        time.sleep(5)  # Wait for the app to open
        scroll()
        gfx_command = f"adb shell dumpsys gfxinfo {package_name.split('/')[0]} > {selected_app}.txt"
        os.system(gfx_command)
        print(f"Collected graphics info for {selected_app}")
        time.sleep(5)  # Wait before proceeding to the next app

print("All selected apps opened and graphics info collected.")

#import openpyxl

# List of app package names


# Create a new Excel workbook and select the active sheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
app_packages = [f"{selected_app}.txt" for selected_app in apps]

for app_package in app_packages:
    try:
        # Define the filename based on the app package name
        filename = f"{app_package}"
        #print(filename)
        # Open and process the file if it exists
        def load_file(filename: str):
            with open(filename) as text_file:
                janky_frames_value = None  # Initialize a variable to store "Janky frames" value
                for line in text_file:
                    if "Total frames rendered:" in line:
                        value = line.strip().split(":")
                        worksheet.append(["Total frames rendered", value[1]])
                    elif "Janky frames:" in line:
                        janky_frames_value = line.split(":")[-1].strip()
                    elif "95th percentile:" in line:
                        value = line.split(":")[-1].strip()
                        worksheet.append(["95th percentile", value])
                        if janky_frames_value is not None:
                            worksheet.append(["Janky frames", janky_frames_value])
        load_file(app_package)
        # for filename in app_packages:
        #     loaded_file.append(load_file(filename))


    except FileNotFoundError:
        print(f"File not found for {app_package}. Skipping...")

# Save the Excel file
workbook.save('output.xlsx')


