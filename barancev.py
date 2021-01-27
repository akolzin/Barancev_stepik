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
    wd = webdriver.Edge("C:\\tools\\msedgedriver.exe")
    #wd1 = webdriver.Chrome()
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
    driver.get("http://localhost/litecart/admin/")
    #driver1.get("http://www.google.com/")
    #wait = WebDriverWait(driver, 10)  # seconds
    #driver.find_element_by_class_name("hOoLGe").click()
    #time.sleep(3)
    driver.find_element_by_name("username").send_keys("admin")
    time.sleep(1)
    driver.find_element_by_name("password").send_keys("admin")
    time.sleep(1)
    #driver.find_element_by_name("q").clear()
    #driver.find_element_by_name("q").send_keys()
    #for _ in range(9):driver.find_element_by_id("K8").click()
    #time.sleep(2)
    #for _ in range(3):driver.find_element_by_id("K49").click()
    #driver.find_element_by_id("K50").click()
    #driver.find_element_by_id("K51").click()
    #time.sleep(2)
    driver.find_element_by_xpath("//button[text()='Login']").click()
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
    time.sleep(1)
    n = 0

    # like = driver.find_elements_by_class_name('app')
    # for x in range(0, len(like)):
    #     if like[x].is_displayed():
    #         like[x].click()

    # while driver.find_element_by_id("box-apps-menu"):
    #     driver.find_element_by_class_name("app").click()
    #     time.sleep(1)
    #     #wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "app")))
    # else:
    #     print('всё!')

    # b = driver.find_elements_by_class_name("app")
    # time.sleep(1)
    # b.click()
    # box-apps-menu > li.app.selected > ul > li.doc.selected > a > span
    # // *[ @ id = "content"] / div / div[1] / text()
    # box-apps-menu > li.app.selected > ul > li.doc.selected
    # box-apps-menu > li.app.selected > ul > li:nth-child(1)
    kl = 0

    mass1 = driver.find_elements_by_css_selector("#box-apps-menu > li")
    print(mass1)
    text_file = open("C:\\Users\\akolzin\\Desktop\\site\\site\\3.txt", "w")
    for x in mass1:
        print('"//span[text()="', x.text, '"]"')
        text_file1 = open('C:\\Users\\akolzin\\Desktop\\site\\site\\3.txt', 'a')
        text_file1.write("//span[text()='")
        text_file1.write(x.text)
        text_file1.write("']" + '\n')
        text_file1.close()

    with open(r"C:\\Users\\akolzin\\Desktop\\site\\site\\3.txt", "r") as file:
        for lin in file:
            print(lin)
            time.sleep(1)
            driver.find_element_by_xpath(lin).click()
            c = []
            c = driver.find_elements_by_css_selector("#box-apps-menu > li.app.selected > ul > li")
            ff = len(c)
            print(ff)
            if ff > 0:
                text_file = open("C:\\Users\\akolzin\\Desktop\\site\\site\\2.txt", "w")
                for x in c:
                    # print('"//p[text()="',x.text,'"]"')
                    text_file = open('C:\\Users\\akolzin\\Desktop\\site\\site\\2.txt', 'a')
                    text_file.write("//span[text()='")
                    text_file.write(x.text)
                    text_file.write("']" + '\n')
                    #text_file = open(r"C:\\Users\\akolzin\\Desktop\\site\\site\\2.txt", "r")
                    text_file.close()
                    #li = text_file.readline()
                    #driver.find_element_by_xpath(li).click()
                with open(r"C:\\Users\\akolzin\\Desktop\\site\\site\\2.txt", "r") as file:
                    for line in file:
                        print(line)
                        time.sleep(1)
                        driver.find_element_by_xpath(line).click()
                        i = driver.find_element_by_xpath("// *[ @ id = 'content'] / div / div[1]")
                        print(i.text)
                        ii = i.text
                        if ii in line:
                            print(ii)
                        else:
                            print("заголовок -", i.text, "не подтвержден")
                            kl = kl + 1
            else:
                i = driver.find_element_by_xpath("// *[ @ id = 'content'] / div / div[1]")
                print(i.text)
                ii = i.text
                if ii in lin:
                    print(ii)
                else:
                    print("заголовок -", i.text, "не подтвержден")
                    kl = kl + 1

    print(kl)
    y = "#box-apps-menu > .app:nth-child(1)"
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(1)").click()
    driver.find_element_by_css_selector(y).click()
    # driver.find_element_by_css_selector("#app > .doc:nth-child(1)").click()
    # driver.find_element_by_css_selector("#app > .doc:nth-child(2)").click()
    # i = driver.find_element_by_xpath("//[@id = 'content'] / div / div[1] / text()")
    # print(i.text)
    driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(2)").click()

    categories = driver.find_elements_by_css_selector("#box-apps-menu > li.app.selected > ul > li")
    print(categories)

    # for x in categories:
    #     driver.find_element_by_link_text(x).click()

    result = [{category.find_element}
              for category in categories]
    print(result)
    # rt = result
    #
    # ty = [{category.get_attribute("href")}
    #       for category in rt]
    # print(ty)

    # mass = []
    # mass2 = []
    # m = None
    # z = 0
    # mass = driver.find_elements_by_css_selector("#box-apps-menu > li.app.selected > ul > li")
    # print(mass)
    # text_file = open("C:\\Users\\akolzin\\Desktop\\site\\site\\2.txt", "w")
    # for x in mass:
    #    #print('"//p[text()="',x.text,'"]"')
    #    text_file = open('C:\\Users\\akolzin\\Desktop\\site\\site\\2.txt', 'a')
    #    text_file.write("//span[text()='")
    #    text_file.write(x.text)
    #    text_file.write("']" + '\n')
    #    text_file.close()

       # text = open("C:\\Users\\akolzin\\Desktop\\site\\site\\2.txt", "r")
       # m = text.readline()
       # print(m)
       # text.close()
       # g = "//span[text()='"
       # h = x.text
       # j = "']"
       # d = g,h,j
       # print(d)
       #os.startfile(r'"C:\\Users\\akolzin\\Desktop\\site\\site\\2.txt"')
       # if z == 1:
       #     time.sleep(1)
       #     driver.find_element_by_xpath(m).click()
       # z = 1
       # f = driver.find_element(By.XPATH, m)
       # time.sleep(1)
       # f.click()

    # with open(r"C:\\Users\\akolzin\\Desktop\\site\\site\\2.txt", "r") as file:
    #     for line in file:
    #         print(line)
    #         time.sleep(1)
    #         driver.find_element_by_xpath(line).click()

    # for x in mass:
    #     driver.find_element_by_xpath("//span[text()='Catalog']").click()
    #     time.sleep(1)
    #     driver.find_element_by_xpath(m).click()

    # print(m)
    # u = "//span[text()='CSV Import/Export']"
    # print(u)
    # driver.find_element_by_xpath(m).click()
    # f = driver.find_element_by_xpath("//span[text()='CSV Import/Export']")
    # time.sleep(2)
    # f.click()
    time.sleep(2)
    # t = driver.find_elements_by_css_selector("#box-apps-menu > li.app.selected > ul > li")
    # for x in t:
    #     print(x.text)

    driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(3)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(4)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(5)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(6)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(7)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(8)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(9)").click()
    # time.sleep(1)
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(10)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(11)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(12)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(13)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(14)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(15)").click()
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(16)").click()
    # time.sleep(2)
    # driver.find_element_by_css_selector("#box-apps-menu > .app:nth-child(17)").click()
    # time.sleep(2)
    # driver.execute_script("location.reload()")
    # driver.refresh()
    driver.get("http://localhost/litecart/")
    r = None
    f = 0
    # box-campaign-products > div > article > a
    # box-campaign-products > div > article > a > div.image-wrapper > div.sticker
    # box-slides

    # // *[ @ id = "box-popular-products"] / div / article[1] / a / div[1] / div
    # // *[ @ id = "box-popular-products"] / div / article[2] / a / div[1] / div
    # // *[ @ id = "box-campaign-products"] / div / article / a / div[1] / div
    # // *[ @ id = "box-campaign-products"] / div / article / a / div[1] / div
    # box-campaign-products > div > article > a > div.image-wrapper > div.sticker

    mas = ["#box-campaign-products > div > article",
          "#box-popular-products > div > article",
          "#box-latest-products > div > article"]
    print(mas)
    jk = 0
    nn = 0
    text_file2 = open("C:\\Users\\akolzin\\Desktop\\site\\site\\4.txt", "w")
    for x in mas:
        # print('"//span[text()="', x.text, '"]"')
        s1 = x
        r = driver.find_elements_by_css_selector(x)
        print('r =', r)
        f = len(r)
        rr = 0
        for x in r:
            mch = ["1","2","3","4","5"]
            text_file2 = open('C:\\Users\\akolzin\\Desktop\\site\\site\\4.txt', 'a')
            text_file2.write(s1)
            text_file2.write(":nth-child(")
            text_file2.write(mch[rr])
            text_file2.write(") > a > div.image-wrapper > div.sticker" + '\n')
            rr = rr + 1
            text_file2.close()
    with open(r"C:\\Users\\akolzin\\Desktop\\site\\site\\4.txt", "r") as file:
        for lines in file:
            print(lines)
            time.sleep(1)
            rk = driver.find_elements_by_css_selector(lines)
            #st = rk.text
            fq = len(rk)
            print('fq =', fq)
            if fq == 1:
                nn = nn + 1
                rk = None
                fq = 0
                assert True
                # if "New" in st:
                #     print("New")
                # else:
                #     if "Sale" in st:
                #         print("Sale")
                #     else:
                #         print("Error")
            else:
                jk = jk + 1
                print("ошибка")
    print(nn)
    print(jk)

    # r = driver.find_elements_by_css_selector(
    #     "#box-campaign-products > div > article > a > div.image-wrapper > div.sticker")
    # print('r =', r)
    # f = len(r)
    # print('f =', f)
    # if  f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-popular-products > div > article:nth-child(1) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-popular-products > div > article:nth-child(2) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-popular-products > div > article:nth-child(3) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-popular-products > div > article:nth-child(4) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-popular-products > div > article:nth-child(5) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-latest-products > div > article:nth-child(1) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-latest-products > div > article:nth-child(2) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-latest-products > div > article:nth-child(3) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-latest-products > div > article:nth-child(4) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True
    # r = driver.find_elements_by_css_selector(
    #     "#box-latest-products > div > article:nth-child(5) > a > div.image-wrapper > div.sticker")
    # f = len(r)
    # if f == 1:
    #     n = n + 1
    #     r = None
    #     f = 0
    #     assert True


    text_file = open("C:\\Users\\akolzin\\Desktop\\site\\site\\1.txt", "w")
    text_file.write(repr(nn))
    time.sleep(1)
    text_file.close()
    os.startfile(r'"C:\\Users\\akolzin\\Desktop\\site\\site\\1.txt"')
    print(nn)

    # try:
    #     elem = driver.find_elements_by_css_selector("#content.image-wrapper:nth-child(1) > .sticker")
    #     return True
    # except NoSuchElementException:
    #     print('Zero element for U!')
    #     return False

    time.sleep(2)
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[text()='OK']"))).click()
    #time.sleep(3)
    #wait.until(EC.title_is("11123 - Поиск в Google"))
    #WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))
