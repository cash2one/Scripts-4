from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(chrome_options=webdriver.ChromeOptions())
driver.get('http://www.google.com')

q = driver.find_element(By.NAME, 'q')
q.send_keys('webdriver')
q.submit()

print driver.title