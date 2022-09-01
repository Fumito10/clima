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
driver.find_element(By.XPATH, '//*[@id="page"]/main/div[4]/div[1]/section[1]/div/ul/li[6]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="term"]').click()
time.sleep(2)
driver.find_element(By.ID, "term").send_keys("Querétaro")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .item-name").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Por horas").click()
