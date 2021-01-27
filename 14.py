import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text_redirect13.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)
    st = browser.find_element(By.NAME, "first_name")
    st.send_keys("st")
    st = browser.find_element(By.XPATH, "//input[@name='last_name' and @class='form-control']")
    st.send_keys("st1")
    st = browser.find_element(By.XPATH, "//input[contains(@class, 'city')]")
    st.send_keys("stm")
    st = browser.find_element(By.CSS_SELECTOR, "input#country.form-control")
    st.send_keys("stn")
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(8)
    browser.quit()