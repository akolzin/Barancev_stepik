

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Tes(unittest.TestCase):
    def setUP(self):
        #self.driver = webdriver.Ie("C:\\tools\IEDriverServer.exe")
        self.driver = webdriver.Chrome()
        ##self.driver.implicitly_wait(30)
        self.driver_url = "http://www.google.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_tes(self):
        driver = self.driver
        driver.get(self.driver_url + "/")
        driver.find_element_by_id("mailbox__login").click()
        driver.find_element_by_id("mailbox__login").send_keys("test")
        driver.find_element_by_id("mailbox__password").clear()
        driver.find_element_by_id("mailbox__password").send_keys("test")
        driver.find_element_by_id("mailbox__auth__button").click()


    def test_example(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.find_element_by_xpath("//button[text()='Login']").click()