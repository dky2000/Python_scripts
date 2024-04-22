import subprocess
import time
import pyautogui
# Specify the path to the Flash tool executable
flash_tool_path = (r"D:\Tools\SP_Flash_Tool_v5.2112_Win\flash_tool.exe")  # Replace with the actual path to your Flash tool

# Run the Flash tool
flash_tool_process = subprocess.Popen(flash_tool_path)
time.sleep(5)
#pyautogui.press('win', 'up')
#pyautogui.typewrite('flash_tool_path')
pyautogui.hotkey('win', 'up')
# Press Enter to open the application
pyautogui.press('enter')
time.sleep(8)
#pyautogui.hotkey('win', 'up')
mouse_position = pyautogui.position()
print("mouse position: ", mouse_position)

# # Define the number of times to press the Tab key
# num_tabs = 7
# #
# # # Simulate pressing the Tab key multiple times
# for _ in range(num_tabs):
#     pyautogui.press('tab')
#     time.sleep(0.3)
#     #pyautogui.press('space'):
# # Check for the Enter key press
# if pyautogui.press('space'):
#      print("Enter key pressed!")
#      time.sleep(6)
#      # print("Enter key not pressed!")
#      # mouse_position = pyautogui.position()
#      # print("Mouse Position:", mouse_position)
# # else:
# # print("Enter key not pressed!")
# # mouse_position = pyautogui.position()
# # print("Mouse Position:", mouse_position)
#
# time.sleep(0.5)
# # file_dialog_x = 716  # Replace with the X-coordinate of the file dialog
# # file_dialog_y = 334  # Replace with the Y-coordinate of the file dialog
# file_dialog_x = 422  # Replace with the X-coordinate of the file dialog
# file_dialog_y = 334
# # Move the mouse to the file dialog and click to activate it
# pyautogui.moveTo(file_dialog_x, file_dialog_y)
# pyautogui.click()
# pyautogui.press('m')
# time.sleep(0.2)
# pyautogui.press('m')
# time.sleep(3)
# pyautogui.press('enter')
#
# time.sleep(6)
# print("Enter key not pressed!")
# mouse_position = pyautogui.position()
# print("Mouse Position:", mouse_position)


# time.sleep(2)  # Adjust the delay as needed
#
#
# file_path = (r'Y:\LIX402_New\release\LIX402-userdebug-2023-06-12-192-Official\MT6761_Android_scatter.txt')  # Replace with the actual path to your file
#
#
# subprocess.Popen(f'explorer "{file_path}"')


