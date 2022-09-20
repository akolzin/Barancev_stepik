import pytest
import time
import requests


def test_example():
    with open("C:\\Users\\akolzin\\Desktop\\softline.txt", "r") as file1:
        # итерация по строкам
        for line in file1:
            print(line.strip())
            # print(line)
            # driver.get("http://frontage.softline.ru.slglobal.stage.slweb.ru/investor-relations")
            # time.sleep(2)
            # driver.quit()
            response = requests.get(line,
                        params={'q': 'requests+language:python'},
                        headers={'Authorization': 'Basic c2hhZWtob3ZhYTo4I1AtVTNuZnBO'},)
            if response.status_code >= 400:
                print(response, 'Not Found.')
            elif response.status_code < 400:
                print(response, 'Success!')
            print()