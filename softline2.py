import pytest
import time
import requests

from selenium import webdriver


@pytest.mark.parametrize("line", ['http://frontage.softline.ru.slglobal.stage.slweb.ru/digital-business/reshenie-tsbr',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/uploads/files/cee2f6/1a5fb7/1cee7e/Leaflet_%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D0%BC%D0%B8_web%2029%2011%202021.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/uploads/files/80eca6/1c20ed/380f1e/SL_FY_2021_es.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/subscribe/checkconfirmnewssubscribe',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/solutions/business-solutions/upravlenie-biznes-protsessami-bpm%20',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/matlab2.php',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/press_s.php?id=11725',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/it_page.php?id=1828',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/about/politika-informatsionnoy-bezopasnosti',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/uploads/f/29/e8/f5/ce/7c/f9/d2/9e/d6/%D0%A3%D0%BC%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%B0%D1%81%D0%BA%D0%B8.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/uploads/files/d586b5/e9f06a/4d58bf/2-video-I-study-at-home-in-Adobe-Premiere.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/press_s.php?id=14690',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/press_s.php?id=14689',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/it_page.php?id=1718',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/video/software-12',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/digital-business/programmno-apparatnyj-kompleks-umnye-kaski',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-new/korporativnoe-licenzirovanie/microsoft-enterprise-agreement',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-new/licenzirovanie-produktov/office-office-365',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/http:/softline.ru/uploads/files/cee2f6/1a5fb7/1cee7e/Leaflet_%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D0%BC%D0%B8_web%2029%2011%202021.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/video/software-51',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/job-in-softline/vacancy-form',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/office_xp',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/uploads/softline-direct-flipbook/Softline-direct%2009-2013',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/video/search',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/press_s.php?id=5085',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/digital-business/servis-provayderam/microsoft-spla',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/comments/clip-270',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/uploads/19/b8/c5/c9/8c/f7/b1/9b/d5/origin.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/microsoft/microsoft-statuses',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/about/news/store.softline.ru/promt/promt-professional-mashinostroenie',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/products/seminars/microsoft.asp?strOvType=prigl',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/about/news/store.softline.ru/paragon/paragon-hard-disk-manager-business',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/softline-leasing',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/uploads/files/e7afa6/0b8cca/6e7b50/Rusiem.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/http:/softline.ru/uploads/f/b8/ad/15/b3/e2/46/2b/8b/81/%D0%9F%D0%BE%D1%80%D1%82%D1%84%D0%BE%D0%BB%D0%B8%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%B2%20-1%D0%A1-%D0%91%D0%B8%D1%82%D1%80%D0%B8%D0%BA%D1%81-.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-new/korporativnoe-licenzirovanie/microsoft-product-and-service-agreement',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/digital-business/servis-provayderam/microsoft-spla/faq-chasto-zadavaemyie-voprosyi-po-spla',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/seminar.asp?catalog_name=SoftLine&category_name=&product_id=Seminar-10175&view=registration',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/communicate',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-total',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/uploads/files/994626/19faab/f994c1/SL_FY_2021_en.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-new/licenzirovanie-produktov',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/comments/clip-1646',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-new/licenzirovanie-produktov/exchange-server',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/news.php?id=9826',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/detail_web/9/1875',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/press_about.php',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-total/go-to-azure',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/solutions/licensing_control.asp',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/http:/softline.ru/uploads/f/24/68/85/d6/4f/5c/72/46/e1/DLP_personalized%20protection%20from%20leaks.pdf',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/video/search/tags/%D0%BF%D1%80%D0%B8%D0%BA%D0%BE%D0%BB',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/it_page.php?id=2047&programma=1',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/press_s.php?id=5512',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-new/licenzirovanie-produktov/system-center',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/product.asp?catalog_name=SoftLine&category_name=&product_id=Software-11272',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-new/korporativnoe-licenzirovanie/microsoft-open-value',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/video/search/tags/Parallels',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/ms-total/microsoft-products/microsoft-teams',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/directorycatalog.php',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/news.asp?catalog_name=SoftLine&product_id=News-12758',
                                    'http://frontage.softline.ru.slglobal.stage.slweb.ru/seminar.asp?catalog_name=SoftLine&category_name=&product_id=Seminar-10229&view=registration'
                                    ])
def test_example(line):
    c = 0
    # driver = webdriver.Chrome("C:\\tools\\chromedriver.exe")
    # driver.get(line)
    file = open("C:\\Users\\akolzin\\Desktop\\softline_error1.txt", "a")
    response = requests.get(line,
                params={'q': 'requests+language:python'},
                headers={'Authorization': 'Basic c2hhZWtob3ZhYTo4I1AtVTNuZnBO'},)
    time.sleep(3)
    if response.status_code >= 400:
        file.write(line.strip() + '\n')
        print(line.strip())
        print(response, 'Not Found.')
    elif response.status_code < 400:
        # print(response, 'Success!')
        c=c+1
    # print(c)
    assert response.status_code < 400
    print(c)
    file.close()