import pytest
import time
import requests


def test_example():
    c=0
    file = open("C:\\Users\\akolzin\\Desktop\\softline3.txt", "w")
    with open("C:\\Users\\akolzin\\Desktop\\softline.txt", "r") as file1:
        # итерация по строкам
        for line in file1:
            # line.rsplit('/', 1)
            f2 = line.rsplit('/', 1)[0]
            # print(line.strip())
            # print(line)
            # driver.get("http://frontage.softline.ru.slglobal.stage.slweb.ru/investor-relations")
            # time.sleep(2)
            # driver.quit()
            response = requests.get(line,
                        params={'q': 'requests+language:python'},
                        headers={'Authorization': 'Basic c2hhZWtob3ZhYTo4I1AtVTNuZnBO'},)
            time.sleep(3)

            if response.status_code >= 400:
                file.write(line.strip() + '\n')
                # print(line.strip())
                # print(response, 'Not Found.')
            elif response.status_code < 400:
                print(response.url)
                print(f2)
                if f2 == response.url:
                    print(line.strip())
                    print(response, 'Success!')
                else:
                    c=c+1
            # print(c)
    print(c)
    file.close()