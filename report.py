import pytest
import time
import requests
import nltk
import pyperclip

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


def test_example(driver):

    driver.get(
        "https://docs.google.com/document/d/1iRIHFmyUdY3xuwhHz6Y7wK0AM_R7t0Mmk_Q6yfHZElo/edit?usp=sharing") # ссылка на документ должна быть расзшарена
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(
        "http://kiwi-interfaces.tass.htc-cs.ru/accounts/login/")
    driver.find_element(By.XPATH, '//input[@id="inputUsername"]').send_keys("akolzin")
    driver.find_element(By.XPATH, '//input[@id="inputPassword"]').send_keys("NfSkf4n2FjsnS4")
    driver.find_element(By.XPATH, '//button[@tabindex="4"]').click()

    time.sleep(3)

    with open("C:\\Users\\akolzin\\Desktop\\report.txt", "r") as file1:
        # итерация по строкам
        for line in file1:
            line1 = "http://kiwi-interfaces.tass.htc-cs.ru/plan/" + line

            driver.get(line1)
            time.sleep(2)
            resul = driver.find_element(By.XPATH, '//input[@id="btn_print"]')
            resul.click()

            driver.execute_script("""
                        let element = document.evaluate("//h1/text()", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); 
                        if (element)
                            element.singleNodeValue.remove(); 
                        """)
            driver.execute_script("""
                        var element = document.querySelector("div.plan_title > div:nth-child(4)");
                        if (element)
                            element.parentNode.removeChild(element);
                        """)
            driver.execute_script("""
                        var element = document.querySelector(".contents");
                        if (element)
                            element.parentNode.removeChild(element);
                        """)
            driver.execute_script("""
                        var element = document.querySelector("#plan_cases");
                        if (element)
                            element.parentNode.removeChild(element);
                        """)

            time.sleep(3)
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").perform()

            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            text = pyperclip.paste()
            list = driver.find_element(By.XPATH, '//canvas[@class="kix-canvas-tile-content"]')
            list.click()
            webdriver.ActionChains(driver).send_keys(Keys.ENTER)
            webdriver.ActionChains(driver).send_keys(Keys.ENTER)
            time.sleep(2)
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").perform()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
    print(text)