import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=
    r"D:\Documents\chromedriver.exe");


driver.get("https://www.clima.com/")
driver.set_window_size(790, 816)
driver.find_element(By.CSS_SELECTOR, ".m_list_countrys_mx > a").click()
driver.find_element(By.CSS_SELECTOR, ".navbar-i-search").click()
driver.find_element(By.ID, "term").send_keys("Querétaro")
driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .item-name").click()
driver.find_element(By.LINK_TEXT, "Por horas").click()
