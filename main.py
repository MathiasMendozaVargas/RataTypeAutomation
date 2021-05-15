import time
import pyautogui
from selenium import webdriver
import keyboard

driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
driver.get("https://www.ratatype.com/")

time.sleep(12)

driver.find_element_by_id("firstType").click()
time.sleep(10)
text = driver.find_element_by_id("str_in").text
keyboard.write(text, delay=0.1)
time.sleep(25)
driver.quit()

