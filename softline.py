import pytest
import time
import requests

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

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
    with open("C:\\Users\\akolzin\\Desktop\\softline.txt", "r") as file1:
        # итерация по строкам
        for line in file1:
            print(line.strip())
            #print(line)
            driver.get()
            # time.sleep(2)
            # driver.quit()
            response = requests.get(line,
                                    params={'q': 'requests+language:python'},
                                    headers={'Authorization': 'Basic c2hhZWtob3ZhYTo4I1AtVTNuZnBO'}, )
            if response.status_code == 404:
                print('Not Found.')
            elif response.status_code < 400:
                print('Success!')
            print(response)
