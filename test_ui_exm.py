from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="добовляем путь")

driver.implicitly_wait(10)
driver.maximize_window()

driver.qet(link)
driver.find_element_by_id("id_name").send_keys("abmin")
driver.find_element_by_id("id_name").send_keys("abmin13")
driver.find_element_by_id("button").click()

driver.close()
driver.quit()
#оставляем пустую строчку
print("Test completed")