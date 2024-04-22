import subprocess

# Run the adb shell monkey command
monkey_command = "adb shell monkey -v --throttle 500 --ignore-crashes --monitor-native-crashes --ignore-timeouts --kill-process-after-error --ignore-security-exceptions -v 500"
subprocess.run(monkey_command, shell=True, check=True)

# Restart the Android device
restart_command = "adb reboot"
subprocess.run(restart_command, shell=True, check=True)