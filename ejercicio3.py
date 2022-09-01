import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=
    r"D:\Documents\chromedriver.exe");

driver.get("https://www.clima.com/")
time.sleep(3)
driver.get("https://www.clima.com/mexico/")
time.sleep(3)
driver.get("https://www.clima.com/mexico/estado-de-queretaro-de-arteaga/")
time.sleep(3)
driver.get("https://www.clima.com/mexico/estado-de-queretaro-de-arteaga/queretaro/")
time.sleep(3)
driver.get("https://www.clima.com/mexico/estado-de-queretaro-de-arteaga/queretaro/por-horas")
time.sleep(3)