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


def test_example(driver):

    # авторизация в гугл
    driver.get("https://docs.google.com/document/u/0/?tgif=d")
    driver.find_element(By.XPATH, '//input[@id="identifierId"]').send_keys("htctesttacc@gmail.com") # htctesttacc@gmail.com HTC test_tacc
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys("Overlor!22")
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(2)

    # скопировать титульник
    driver.get(
        "https://docs.google.com/document/d/17COE2ug0RdCHsyhtL5dKbVCDEADxs62zE4kg6NFRczY/edit?usp=sharing")
    time.sleep(2)
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").perform()

    # создание дока для отчета
    driver.get(
        "https://docs.google.com/document/u/0/?tgif=d") # создание дока для отчета
    driver.find_element(By.XPATH, '//img[@src="https://ssl.gstatic.com/docs/templates/thumbnails/docs-blank-googlecolors.png"]').click()

    # driver.get(
    #     "https://docs.google.com/document/d/1iRIHFmyUdY3xuwhHz6Y7wK0AM_R7t0Mmk_Q6yfHZElo/edit?usp=sharing") # ссылка на документ должна быть расзшарена

    # добавить титульник в созданный документ
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    list = driver.find_element(By.XPATH, '//canvas[@class="kix-canvas-tile-content"]') # kix-stacked-tile-page-shadow
    # list = driver.find_element(By.XPATH, '//*[@id="kix-appview"]/div[7]/div/div[1]/div[1]/div/div/canvas')
    list.click()
    time.sleep(2)
    # webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
    # webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.DELETE).perform()
    # time.sleep(1)
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").perform()

    # авторизация в киви
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(
        "http://kiwi-interfaces.tass.htc-cs.ru/accounts/login/")
    driver.refresh()
    ret = driver.find_element(By.XPATH, '//input[@id="inputUsername"]')
    ret.send_keys("akolzin")
    driver.find_element(By.XPATH, '//input[@id="inputPassword"]').send_keys("NfSkf4n2FjsnS4")
    ret.send_keys("akolzin")
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[@tabindex="4"]').click()

    time.sleep(3)

    # копирование тест-планов в документ
    with open("C:\\Users\\akolzin\\Desktop\\report.txt", "r") as file1:  # открыть файл с id тест-планов
        # итерация по строкам
        for line in file1:
            line1 = "http://kiwi-interfaces.tass.htc-cs.ru/plan/" + line  # формируется URL тест-плана

            # открыть тест-план
            driver.get(line1)
            time.sleep(2)
            # нажать "Печатать план"
            resul = driver.find_element(By.XPATH, '//input[@id="btn_print"]')
            resul.click()

            # парсинг спраницы печати
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

            # копирование страницы печати
            time.sleep(3)
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").perform()

            # возврат в гугл документу и добавление тест-кейсов в документ
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            text = pyperclip.paste()
            list = driver.find_element(By.XPATH, '//canvas[@class="kix-canvas-tile-content"]')
            list.click()
            # webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).perform()
            # webdriver.ActionChains(driver).send_keys(Keys.ENTER)
            time.sleep(2)
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").perform()
            time.sleep(2)
            # webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).perform()
            driver.switch_to.window(driver.window_handles[1])
    # обновить содержание в документе
    driver.switch_to.window(driver.window_handles[0])
    current_url1 = driver.current_url
    # print(current_url1)
    # driver.close()
    # time.sleep(1)
    # driver.close()
    # time.sleep(3)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(current_url1)
    time.sleep(3)
    # list1 = driver.find_element(By.XPATH, '//*[@id="kix-appview"]/div[7]/div/div[1]/div[1]/div/div[2]')
    # time.sleep(1)
    # list1.click()
    # time.sleep(2)

    i = 0
    while i < 40:
        webdriver.ActionChains(driver).send_keys(Keys.DOWN).perform()
        i = i + 1

    time.sleep(3)
    list2 = driver.find_element(By.XPATH, '//*[@id="kix-appview"]/div[7]/div/div[4]/div')
    time.sleep(1)
    list2.click()

    # указать название документа
    time.sleep(1)
    title = driver.find_element(By.XPATH, '//*[@id="docs-title-widget"]/input')
    webdriver.ActionChains(driver).send_keys(Keys.DELETE).perform()
    title.clear()
    time.sleep(2)
    title.send_keys("Заявка 20 // Методика тестирования (ПМИ)")
    print(text)


def test_example1233(driver):  # черновой код для теста отдельных функций

    # авторизация в гугл
    driver.get("https://docs.google.com/document/u/0/?tgif=d")
    driver.find_element(By.XPATH, '//input[@id="identifierId"]').send_keys(
        "htctesttacc@gmail.com")  # htctesttacc@gmail.com HTC test_tacc
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys("Overlor!22")
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(2)

    driver.get("https://docs.google.com/document/d/1w7GCeKvQU6JBW0n-K872AXKCoQecjQ-OvAKy3dDbmwo/edit#")
    time.sleep(1)

    title = driver.find_element(By.XPATH, '//*[@id="docs-title-widget"]/input')
    webdriver.ActionChains(driver).send_keys(Keys.DELETE).perform()
    title.clear()
    time.sleep(2)
    title.send_keys("Заявка 20 // Методика тестирования (ПМИ)")

    time.sleep(3)
    # clipboard.copy("Заявка 20 // Методика тестирования (ПМИ)")
    # title.click()
    # webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").perform()