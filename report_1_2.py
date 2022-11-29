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


def test_example_ppi(driver):  # копирование названий тест-кейсов и запись в файл

    driver.get(
        "http://kiwi-interfaces.tass.htc-cs.ru/accounts/login/")
    driver.find_element(By.XPATH, '//input[@id="inputUsername"]').send_keys("akolzin")
    driver.find_element(By.XPATH, '//input[@id="inputPassword"]').send_keys("NfSkf4n2FjsnS4")
    driver.find_element(By.XPATH, '//button[@tabindex="4"]').click()

    time.sleep(3)
    file = open("C:\\Users\\akolzin\\Desktop\\пми.txt", "w")  # файл для запись тест-планов
    with open("C:\\Users\\akolzin\\Desktop\\report.txt", "r") as file1:  # файл с номерами тест-планов
        # итерация по строкам
        for line in file1:
            line1 = "http://kiwi-interfaces.tass.htc-cs.ru/plan/" + line

            driver.get(line1)
            time.sleep(2)
            resul = driver.find_element(By.XPATH, '//input[@id="btn_print"]')
            resul.click()

            #  запись названия тест-плана
            list = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/h1/b').text
            file.write(list)
            file.write('\n')

            #  элементы названий кейсов
            count = driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div/ol/li')
            print(len(count))

            i = 0
            while i < len(count):  #  запись названий кейсов последовалельно
                ceis = count[i].text
                ceis_str = ceis.replace(', ПОДТВЕРЖДЕНО', '')
                ceis_str3 = ceis_str.split(' ', 1)[-1]
                file.write(ceis_str3 + '\n')
                print(ceis_str3)
                # res_str = ceis_str[:0] + ceis_str[3:]
                # res_str1 = res_str.replace(':', '', 1)
                # res_str2 = res_str1.split(' ', 1)
                # file.write(res_str2[0] + '\n')
                # print(res_str2[0])
                i = i + 1

            file.write('\n')

            i = 0
            while i < len(count):  #  запись номеров кейсов последовалельно
                ceis = count[i].text
                ceis_str = ceis.replace(', ПОДТВЕРЖДЕНО', '')
                # ceis_str3 = ceis_str.split(' ', 1)[-1]
                # file.write(ceis_str3 + '\n')
                # print(ceis_str3)
                res_str = ceis_str[:0] + ceis_str[3:]
                res_str1 = res_str.replace(':', '', 1)
                res_str2 = res_str1.split(' ', 1)
                file.write(res_str2[0] + '\n')
                print(res_str2[0])
                i = i + 1

            file.write('\n')
    print(list)
