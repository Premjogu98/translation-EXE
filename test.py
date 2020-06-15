from selenium import webdriver
# from pynput.keyboard import Key, Controller
import time
# import pyautogui
browser = webdriver.Chrome(executable_path=str("D:\\Translation EXE\\chromedriver.exe"))
browser.maximize_window()
time.sleep(2)
browser.get('https://translate.google.com/')

a = True
while a == True:
    for i1 in browser.find_elements_by_xpath('//*[@id="source"]'):
        i1.clear()
        i1.send_keys('Ctrl + F5 Buttons Going To Press')
        break
    print('After 10 Sec Pressing Ctrl + F5')
    time.sleep(10)
    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("f5")
    # pyautogui.keyUp("f5")
    # pyautogui.keyUp("ctrl")
    browser.delete_all_cookies()
    time.sleep(3)
    print('Just Pressed Ctrl + F5')
    print('===========================================================================================\n')
    for i2 in browser.find_elements_by_xpath('//*[@id="source"]'):
        i2.clear()
        i2.send_keys('Shift + F5 Buttons Going To Press')
        break
    print('After 10 Sec Pressing Shift + F5')
    time.sleep(10)
    # pyautogui.keyDown("shift")
    # pyautogui.keyDown("f5")
    # pyautogui.keyUp("f5")
    # pyautogui.keyUp("shift")
    browser.delete_all_cookies()
    print('Just Pressed Shift + F5')
    time.sleep(2)
    print('===========================================================================================\n')
    for i3 in browser.find_elements_by_xpath('//*[@id="source"]'):
        i3.clear()
        i3.send_keys('ctrl + Shift + r Buttons Going To Press')
        break
    print('After 10 Sec Pressing ctrl + Shift + r')
    time.sleep(10)
    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("shift")
    # pyautogui.keyDown("r")
    # pyautogui.keyUp("r")
    # pyautogui.keyUp("shift")
    # pyautogui.keyUp("ctrl")
    browser.delete_all_cookies()
    print('Just Pressed ctrl + Shift + r')
    print('===========================================================================================\n')
    time.sleep(5)
    # time.sleep(5)
    a = True
