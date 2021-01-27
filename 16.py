import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(desired_capabilities={"chromeOptions":{"args":["--start-fullscreen"]}})
#driver = webdriver.Firefox()
print(driver.capabilities)
time.sleep(2)

driver.get("http://www.google.com/")
time.sleep(1)
#driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + '\t')
driver.execute_script("window.open('http://yandex.ru/','_blank');")
time.sleep(1)
# переключиться на новую вкладку (с индексом 1)
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.get("http://www.google.com/")
# если необходимо
# вернуться на предыдущую вкладку (с индексом 0)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
textarea = driver.find_element_by_name("q")
time.sleep(1)
textarea.send_keys("webdriver")
time.sleep(1)
submit_button = driver.find_element_by_class_name("gNO89b")
time.sleep(1)
submit_button.click()
time.sleep(1)
driver.execute_script("alert('Robots at work')")
time.sleep(1)
alert = driver.switch_to.alert
alert.accept()
time.sleep(1)
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)
time.sleep(1)