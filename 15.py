import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(desired_capabilities={"chromeOptions":{"args":["--start-fullscreen"]}})
print(driver.capabilities)
time.sleep(2)

driver.get("http://www.google.com/")
time.sleep(1)
driver.find_element_by_class_name("hOoLGe").click()
time.sleep(3)
textarea = driver.find_element_by_name("q")
time.sleep(1)
textarea.send_keys("webdriver")
time.sleep(1)
for _ in range(9): driver.find_element_by_id("K8").click()
time.sleep(2)
for _ in range(3): driver.find_element_by_id("K49").click()
driver.find_element_by_id("K50").click()
driver.find_element_by_id("K51").click()
time.sleep(2)
submit_button = driver.find_element_by_class_name("gNO89b")
time.sleep(1)
submit_button.click()

time.sleep(2)
for _ in range(3):
  driver.execute_script('window.scrollTo(0,1500);')
  time.sleep(1)
  driver.execute_script('window.scrollTo(0,300);')
  time.sleep(1)
  driver.execute_script('window.scrollTo(0,0);')

#driver.execute_script("alert('Robots at work')")
#driver.find_element_by_link_text("OK").click()
time.sleep(3)
driver.execute_script("location.reload()")
driver.refresh()
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[text()='OK']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))


#def driver(request):
  #  wd = webdriver.Firefox()
  #  time.sleep(10)
  #  print(wd.capabilities)
  #  request.addfinalizer(wd.quit)
  #  return wd


#def test_example(driver):
  #  driver.get("http://www.google.com/")
  #  time.sleep(10)
  #  driver.find_element_by_name("q").send_keys("webdriver")
  #  time.sleep(10)
  #  driver.find_element_by_name("btnG").click()
  #  WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))