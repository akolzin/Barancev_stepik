import subprocess
import pytest
import time
import os
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import wait
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    #wd = webdriver.Ie("C:\\tools\\IEDriverServer.exe")
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
    # driver.switch_to_window(driver.current_window_handle)
    # driver.execute_script("window.focus();")
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    time.sleep(1)
    driver.find_element_by_name("password").send_keys("admin")
    #time.sleep(2)
    driver.find_element_by_xpath("//button[text()='Login']").click()
    time.sleep(3)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_css_selector("#box-apps-menu > li:nth-child(3)").click()
    mass = driver.find_elements_by_css_selector(
        "#content > div > div.panel-body > form > table > tbody > tr")
    #text_file = open("C:\\Users\\akolzin\\Desktop\\site\\site\\5.txt", "w")
    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = 0
    j = 0
    jn = 0
    f = len(mass)
    for x in mass:
        print(x.text)
        # s = x.text
        # s = [val for ind, val in enumerate(re.split(r"\s+", s)) if (ind + 1) % 3 == 0]

        #print(" ".join(s1))
        #print(s)
        # ss = " ".join(s)
        # f1 = len(x.text)
        # f1 = f1 - 1
        #print(f1)
        # s1 = x.text[f1]
        last = x.text.split()[-1]
        print(last)
        pp = x.text.split(' ', 2)[2]
        p = '' if ' ' not in pp else pp.rsplit(' ', 1)[0]
        print(p)

        if last != "0":
            n1 = 0
            j1 = 0
            # driver.find_element_by_link_text(ss).click()
            href = driver.find_element_by_link_text(p).get_attribute("href")
            # rt = x.find_element_by_xpath("// td[5] / a[@href]").get_attribute('href')
            # print(rt)
            print(href)
            driver.execute_script("window.open('http://yandex.ru/','_blank');")
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[1])
            driver.get(href)
            time.sleep(1)
            # content > div > div.panel-body > form > table > tbody > tr
            mass2 = driver.find_elements_by_css_selector(
                "#content > div > div.panel-body > form > table > tbody > tr")

            f = len(mass2)
            rf = 0
            for x1 in mass2:
                rf = rf + 1
                text_file2 = open('C:\\Users\\akolzin\\Desktop\\site\\site\\5.txt', 'w')
                text_file2.write("zones[")
                text_file2.write(x1.text)
                #text_file2.write(str(rf))
                text_file2.write("][name]")
                text_file2 = open(r"C:\\Users\\akolzin\\Desktop\\site\\site\\5.txt", "r")
                ed = text_file2.readline()
                print(ed)
                text_file2.close()
                print(x1.text)
                rr = driver.find_element_by_name(ed).get_attribute("value")
                print(rr)
                yu1 = rr[0]
                print(yu1)
                if yu1 == l1[n1]:
                    j1 = j1 + 1
                else:
                    n1 = n1 + 1
                    j1 = j1 + 1
                    while yu1 != l1[n1]:
                        n1 = n1 + 1
                    if yu1 != l1[n1]:
                        print("error-----------------------------------------------------1")
            time.sleep(1)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        yu = p[0]
        print(yu)
        if yu == al[n]:
            j = j + 1
        else:
            n = n + 1
            j = j + 1
            while yu != al[n]:
                n = n + 1
            if yu != al[n]:
                print("error--------------------------------------------------")
    if f == j:
        print(f, j, "namana")
    else:
        print(f, j)
        print(n)
        print("error or namana")
        # text_file1 = open('C:\\Users\\akolzin\\Desktop\\site\\site\\5.txt', 'a')
        # text_file1.write("//span[text()='")
        # text_file1.write(x.text)
        # text_file1.write("']" + '\n')
        # text_file1.close()  #content > div > div.panel-body > form > table > tbody > tr:nth-child(243)