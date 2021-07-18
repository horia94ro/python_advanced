from selenium import webdriver
import time

chrome = None
try:
    chrome = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    chrome.maximize_window()
    chrome.get("https://google.com")
    time.sleep(5)
    #Avem metode care ne permit identificarea prin diverse atribute, dar in cazul nostru se vom folosi de id/name
    #In mod alternativ  am putea folosi chiar find_element_by_xpath()

    """Identificăm butonul de I agree"""
    agree_button = chrome.find_element_by_id("L2AGLb")
    agree_button.click()
    time.sleep(5)
    """Identificăm bara de căutare"""
    search_bar = chrome.find_element_by_name("q")
    """Trimitem textul pe care vrem să îl căutăm"""
    search_bar.send_keys("cursuri telacad")
    time.sleep(5)
    """Apăsăm pe butonul de căutare"""
    search_button = chrome.find_element_by_name("btnK")
    search_button.click()
    time.sleep(10)
except Exception as e:
    print(repr(e))
finally:
    #Ne asigurăm ca sesiunea de webdriver nu rămâne deschisă în cazul în care apar excepții la rulare
    if chrome: chrome.quit()
