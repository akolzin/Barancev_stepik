import subprocess
import pytest
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import wait
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    #wd1 = webdriver.Ie("C:\\tools\\IEDriverServer.exe")
    #wd = webdriver.Firefox()
    #wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
    #wd = webdriver.Edge("C:\\tools\\msedgedriver.exe")
    wd = webdriver.Chrome()
    #wd = webdriver.Ie(capabilities={"requireWindowFocus": True})

    # dri = webdriver.Ie("C:\\tools\\IEDriverServer.exe")
    # dri.get("http://www.google.com/")
    # textarea = dri.find_element_by_name("q")
    # textarea.send_keys("webdriver")
    # submit_button = dri.find_element_by_class_name("gNO89b")
    # time.sleep(1)
    # submit_button.click()
    # dri.quit()
    #
    # dri1 = webdriver.Edge("C:\\tools\\msedgedriver.exe")
    # dri1.get("http://www.google.com/")
    # textarea1 = dri1.find_element_by_name("q")
    # textarea1.send_keys("webdriver")
    # submit_button1 = dri1.find_element_by_class_name("gNO89b")
    # time.sleep(1)
    # submit_button1.click()
    # dri1.quit()
    #
    # dri2 = webdriver.Chrome()
    # dri2.get("http://www.google.com/")
    # textarea2 = dri2.find_element_by_name("q")
    # textarea2.send_keys("webdriver")
    # submit_button2 = dri2.find_element_by_class_name("gNO89b")
    # time.sleep(1)
    # submit_button2.click()
    # dri2.quit()

    # subprocess.Popen(('start', 'C:\\Users\\akolzin\\Desktop\\site\\site\\1.txt'), shell=True)
    # dri3 = webdriver.Firefox()
    # dri3.get("http://www.google.com/")
    # textarea3 = dri3.find_element_by_name("q")
    # textarea3.send_keys("webdriver")
    # submit_button3 = dri3.find_element_by_class_name("gNO89b")
    # time.sleep(1)
    # submit_button3.click()
    # dri3.quit()

    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd



def test_example(driver):
    driver.switch_to_window(driver.current_window_handle)
    driver.execute_script("window.focus();")
    driver.get("http://media.test.itass.local/clients/customers")
    #wait = WebDriverWait(driver, 10)  # seconds
    time.sleep(2)
    driver.find_element_by_id("details-button").click()
    driver.find_element_by_id("proceed-link").click()
    #driver.get("http://media.test.itass.local")
    driver.find_element_by_id("userNameInput").send_keys("ext_kolzin_a")
    time.sleep(1)
    driver.find_element_by_id("passwordInput").send_keys("")
    driver.find_element_by_id("submitButton").click()
    time.sleep(2)
    driver.find_element_by_class_name("LGPPtbfSgKkHeKMeSjFv2").click()
    #time.sleep(3)
    driver.find_element_by_id("name").send_keys("admin")
    time.sleep(1)
    driver.find_element_by_id("email").send_keys("admin@dsfgsg.df")
    time.sleep(1)
    driver.execute_script('window.scrollTo(0,300);')
    time.sleep(1)
    driver.find_element_by_css_selector("#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > section:nth-child(3) > section > div > div:nth-child(7) > div > div > div > div > div > svg").click()
    driver.find_element_by_class_name("_2L3E4ziW_4O8Dr95BBr2YU").click()
    #time.sleep(2)
    driver.find_element_by_id("phone1").send_keys("1212")
    driver.find_element_by_id("inn").send_keys("903322445522")
    driver.find_element_by_id("kpp").send_keys("22222249")
    #driver.find_element_by_css_selector("div.FPdoLc.tfB0Bf > center > input[name=\"btnK\"]").click()
    #submit_button = driver.find_element_by_class_name("gNO89b")
    time.sleep(2)
    #submit_button.click()
    # for _ in range(2):
    #     driver.execute_script('window.scrollTo(0,1500);')
    #     time.sleep(1)
    #     driver.execute_script('window.scrollTo(0,300);')
    #     time.sleep(1)
    #     driver.execute_script('window.scrollTo(0,0);')
    #     time.sleep(1)
    #driver.execute_script("alert('Robots at work')")

    driver.find_element_by_css_selector("#root > div > div > div.MDTTD808z7GuhtYhNCiyx > form > div.IKVnscL2xZb4_HAppSRik > div > div > button._1JPTNwXTDV_vLByphy1l-O.M9c1UcWhIvzGEP-ZtlSLa._2bMXaBwkLZj8rpG7EdgcRt").click()
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,0);')
    time.sleep(5)
