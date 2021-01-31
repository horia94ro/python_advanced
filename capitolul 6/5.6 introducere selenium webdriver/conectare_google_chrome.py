from selenium import webdriver
import time

chrome = webdriver.Chrome(executable_path="C:\\chromedriver.exe") #in mod alternativ se poate crea o instanta a altui browser(Firefox), indicand driver-ul specific
chrome.get("https://telacad.ro")
time.sleep(10)
chrome.quit()