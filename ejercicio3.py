import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=
    r"D:\Documents\chromedriver.exe");


driver.get("https://www.clima.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.set_window_size(790, 816)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".m_list_countrys_mx > a").click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="page"]/header/div[2]/div[3]/ul/li/button').click()
time.sleep(2)
driver.find_element(By.ID, "term").send_keys("Querétaro")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .item-name").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Por horas").click()
