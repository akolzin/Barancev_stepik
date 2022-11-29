import pytest
import time
import requests
import nltk
import pyperclip
import clipboard

from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from bs4 import BeautifulSoup

@pytest.fixture
def driver(request):
    #wd = webdriver.Firefox()
    #wd = webdriver.Edge("C:\\tools\\msedgedriver.exe")
    wd = webdriver.Chrome("C:\\tools\\chromedriver.exe")
    #wd = webdriver.Ie("C:\\tools\\IEDriverServer.exe")
    #wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):  # копирование названий тест-кейсов и запись в файл

    driver.get(
        "http://kiwi-interfaces.tass.htc-cs.ru/accounts/login/")
    driver.find_element(By.XPATH, '//input[@id="inputUsername"]').send_keys("akolzin")
    driver.find_element(By.XPATH, '//input[@id="inputPassword"]').send_keys("NfSkf4n2FjsnS4")
    driver.find_element(By.XPATH, '//button[@tabindex="4"]').click()

    time.sleep(3)
    file = open("C:\\Users\\akolzin\\Desktop\\пми.txt", "w")
    with open("C:\\Users\\akolzin\\Desktop\\report.txt", "r") as file1:
        # итерация по строкам
        for line in file1:
            line1 = "http://kiwi-interfaces.tass.htc-cs.ru/plan/" + line

            driver.get(line1)
            time.sleep(2)
            resul = driver.find_element(By.XPATH, '//input[@id="btn_print"]')
            resul.click()

            driver.execute_script("""
                        var element = document.querySelector("div.plan_title > div:nth-child(4)");
                        if (element)
                            element.parentNode.removeChild(element);
                        """)
            driver.execute_script("""
                        var element = document.querySelector("body > div:nth-child(2)"); 
                        if (element)
                            element.parentNode.removeChild(element);
                        """)
            driver.execute_script("""
                        var element = document.querySelector("div.contents > h3"); 
                        if (element)
                            element.parentNode.removeChild(element);
                        """)

            time.sleep(2)
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").perform()

            text = pyperclip.paste()
            res_str = text.replace(', ПОДТВЕРЖДЕНО', '')
            file.write(res_str.strip() + '\n' + '\n')
            file.write('\n')
        file.write('\n')
    print(text)


def test_example1(driver):   # удаление отступов
    file = open("C:\\Users\\akolzin\\Desktop\\пми1.txt", "w")
    with open("C:\\Users\\akolzin\\Desktop\\пми.txt", "r") as file1:
        for line in file1:
            if len(line) > 1:
                res_str3 = line.split(' ', 1)[-1]
                file.write(res_str3.strip() + '\n')


def test_example2(driver):   # копирование из файла в документ
    with open("C:\\Users\\akolzin\\Desktop\\пми1.txt", "r") as file1:
        driver.get(
            "https://docs.google.com/document/d/1iRIHFmyUdY3xuwhHz6Y7wK0AM_R7t0Mmk_Q6yfHZElo/edit?usp=sharing")
        int_number = file1.read()
        print(int_number)
        clipboard.copy(int_number)
        list = driver.find_element(By.XPATH, '//canvas[@class="kix-canvas-tile-content"]')
        list.click()
        time.sleep(1)
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").perform()
        time.sleep(1)
        # for line in file1:
        #     clipboard.copy(line)
        #     print(line)
        #     list = driver.find_element(By.XPATH, '//canvas[@class="kix-canvas-tile-content"]')
        #     list.click()
        #     time.sleep(1)
        #     webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").perform()
