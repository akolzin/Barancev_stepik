import pytest
import time
import requests


def test_example():

    file = open("C:\\Users\\akolzin\\Desktop\\softline_doc.txt", "w")
    with open("C:\\Users\\akolzin\\Desktop\\softline1.txt", "r") as file1:
        # итерация по строкам
        for line in file1:
            file.write("'" + line.strip() + "'," + '\n')
            print(line.strip())
    file.close()