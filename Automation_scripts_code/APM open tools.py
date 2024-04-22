import subprocess
import time
import pyautogui
flash_tool_path = (r"D:\Tools\SP_Flash_Tool_v5.2112_Win\flash_tool.exe")  # Replace with the actual path to your Flash tool

# Run the Fla
# sh tool
# sh tool
flash_tool_process = subprocess.Popen(flash_tool_path)
time.sleep(8)
mm
pyautogui.hotkey('win', 'up')
# Press Enter to open the application
pyautogui.press('enter')
time.sleep(4)

num_tabs = 7
#
# # Simulate pressing the Tab key multiple times
for _ in range(num_tabs):
    pyautogui.press('tab')
    time.sleep(0.3)
if pyautogui.press('space'):
     print("Enter key pressed!")
time.sleep(0.5)
file_dialog_x = 422
file_dialog_y = 334
pyautogui.moveTo(file_dialog_x, file_dialog_y)
pyautogui.click()
pyautogui.press('m')
time.sleep(0.2)
pyautogui.press('m')
time.sleep(1)
pyautogui.press('enter')
time.sleep(4)
file_dialog_x = 326
file_dialog_y = 262
pyautogui.moveTo(file_dialog_x, file_dialog_y)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)


pyautogui.press('up')
time.sleep(0.5)
pyautogui.press('up')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'd')
mouse_position = pyautogui.position()
print("mouse position: ", mouse_position)

