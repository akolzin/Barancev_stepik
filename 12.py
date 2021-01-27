import pytest
import time

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
    #wd = webdriver.Chrome()
    wd = webdriver.Ie("C:\\tools\\IEDriverServer.exe")
    #wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    wait = WebDriverWait(driver, 10)  # seconds
    driver.find_element_by_class_name("hOoLGe").click()
    time.sleep(3)
    driver.find_element_by_name("q").send_keys("webdriver")
    time.sleep(2)
    #driver.find_element_by_name("q").clear()
    #driver.find_element_by_name("q").send_keys()
    for _ in range(9):driver.find_element_by_id("K8").click()
    time.sleep(2)
    for _ in range(3):driver.find_element_by_id("K49").click()
    driver.find_element_by_id("K50").click()
    driver.find_element_by_id("K51").click()
    time.sleep(2)
    driver.find_element_by_class_name("gNO89b").click()
    #driver.find_element_by_css_selector("div.FPdoLc.tfB0Bf > center > input[name=\"btnK\"]").click()
    #submit_button = driver.find_element_by_class_name("gNO89b")
    time.sleep(3)
    #submit_button.click()
    for _ in range(3):
        driver.execute_script('window.scrollTo(0,1500);')
        time.sleep(1)
        driver.execute_script('window.scrollTo(0,300);')
        time.sleep(1)
        driver.execute_script('window.scrollTo(0,0);')
        time.sleep(1)
    #driver.execute_script("alert('Robots at work')")
    time.sleep(1)
    driver.execute_script("location.reload()")
    driver.refresh()
    time.sleep(2)
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[text()='OK']"))).click()
    time.sleep(3)
    wait.until(EC.title_is("11123 - Поиск в Google"))
    #WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))