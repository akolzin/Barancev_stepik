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

    # requests.post("http://kiwi-interfaces.tass.htc-cs.ru/accounts/login/",
    #                         data={ 'csrfmiddlewaretoken': "fF6EaOa7bldzxLud46LfRoYfEWRn97vuV769GDaHAZuXdD7E4y5PwGYLYF44DKfO",
    #
    #                                 'username': "akolzin",
    #                                 'password': "NfSkf4n2FjsnS4"},
    #                         headers={
    #                             'Cookie': 'csrftoken=SyNpR7fEToW1bUHWrgxTGc5tfLjwZwBwAWSyA32L6jWrAUNFJfmr6qgmBWgVuSIG'},
    #              )

    # str = "pythonist1 pythonist2 pythonist3 pythonist4"
    # print("Исходная строка: " + str)
    # # Удаляем элемент с индексом 3
    # # с помощью срезов и объединения
    # res_str = str[:11] + str[33:]
    # print("Строка после удаления символа: " + res_str)

    driver.get(
        "https://docs.google.com/document/d/1iRIHFmyUdY3xuwhHz6Y7wK0AM_R7t0Mmk_Q6yfHZElo/edit?usp=sharing")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(
        "http://kiwi-interfaces.tass.htc-cs.ru/accounts/login/")
    driver.find_element(By.XPATH, '//input[@id="inputUsername"]').send_keys("akolzin")
    driver.find_element(By.XPATH, '//input[@id="inputPassword"]').send_keys("NfSkf4n2FjsnS4")
    driver.find_element(By.XPATH, '//button[@tabindex="4"]').click()

    driver.get("http://kiwi-interfaces.tass.htc-cs.ru/plans/printable/",
                                    data={'plan': 93},
                                    headers={'Cookie': 'sessionid=r5l58bokevmcnpeleknqiueeratc3k4o; csrftoken=WrR2eWmKGOVwNmhUJrRd9UGV9agP4MfaAnz1efDnCBzjnfkXHFGlcMj5ubxtllCE'}, )
    time.sleep(9)

    with open("C:\\Users\\akolzin\\Desktop\\report.txt", "r") as file1:
        # итерация по строкам
        for line in file1:

            driver.get(line)
            time.sleep(2)
            resul = driver.find_element(By.XPATH, '//input[@id="btn_print"]')
            resul.click()

            # resul1 = driver.find_element(By.XPATH, '//div[@class="contents"]')
            # resul1.remove()
            # resul2 = driver.find_element(By.XPATH, '//html/body/div[1]/div[4]')
            # resul2.clear()

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


            time.sleep(9)
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").perform()

            # body = driver.find_element_by_tag_name("body")
            # body.send_keys(Keys.CONTROL + 't')
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            # pyperclip.paste()
            text = pyperclip.paste()
            list = driver.find_element(By.XPATH, '//canvas[@class="kix-canvas-tile-content"]')
            list.click()
            # webdriver.ActionChains(driver).send_keys("ENTER").perform()
            webdriver.ActionChains(driver).send_keys(Keys.ENTER)
            # webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
            # webdriver.ActionChains(driver).send_keys("ENTER").perform()
            # time.sleep(2)
            time.sleep(2)
            webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").perform()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
    print(text)

    # with open('test.docx', 'w') as output_file:
    #     output_file.write(text)
    #
    #
    # response = requests.post("http://kiwi-interfaces.tass.htc-cs.ru/plans/printable/",
    #                                 data={'plan': 93},
    #                                 headers={'Cookie': 'csrftoken=ioFau0nXcc1ZvxbLxysZ3xUbO0yrPK0ce6aTSd4nMIbBZ0faAmsQ6m5xeaDnvGZQ; sessionid=eppg3cb2qwld5gdkadcz8ltgb68o1rt7'}, )
    # with open('test.html', 'w') as output_file:
    #     output_file.write(response.text)
    # raw = nltk.clean_html(response)
    # print(raw)
    # print(response.text)


    # with open("C:\\Users\\akolzin\\Desktop\\softline.txt", "r") as file1:
    #     # итерация по строкам
    #     for line in file1:
    #         print(line.strip())
    #         #print(line)
    #         driver.get(
    #             "http://kiwi-interfaces.tass.htc-cs.ru/plan/93/dorabotka-popapa-dobavit-v-peremestit-v-vybor-konteinera#testcases")
    #         # time.sleep(2)
    #         # driver.quit()
    #         response = requests.get(line,
    #                                 params={'q': 'requests+language:python'},
    #                                 headers={'Authorization': 'Basic c2hhZWtob3ZhYTo4I1AtVTNuZnBO'}, )
    #         if response.status_code == 404:
    #             print('Not Found.')
    #         elif response.status_code < 400:
    #             print('Success!')
    #         print(response)
