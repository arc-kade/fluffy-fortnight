import requests
import pandas as pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://books.toscrape.com")
time.sleep(3)
books=driver.find_elements(By.CLASS_NAME,"product_pod")
print("number of books: ",len(books))
for i in books:
    print(i.text)
driver.quit()
