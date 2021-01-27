import pytest
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Ie()
driver.get("http://localhost/litecart/")

try:
     elem = driver.find_elements_by_css_selector("#content.image-wrapper:nth-child(1) > .sticker")
     #return True
except NoSuchElementException:
     print('Zero element for U!')
     #return False