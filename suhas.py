# import time
# from xml.etree.ElementPath import xpath_tokenizer
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.maximize_window()
#
# driver.get("https://www.expedia.com/")
# driver.implicitly_wait(5)
# driver.find_element(By.CLASS_NAME,'uitk-tab-anchor uitk-tab-anchor-selected')
#
# driver.find_element(By.ID,'origin_select-input').send_keys("Mangalore")
#
# time.sleep(50)
#
# driver.find_element(By.XPATH,"//*[@id='FlightSearchForm_ROUND_TRIP']").send_keys("Bangalore")
#
# # driver.find_element("uitk-fake-input uitk-form-field-trigger uitk-field-fake-input uitk-field-fake-input-hasicon").send_keys("May 11 - May 18").clear()
# driver.find_element(By.XPATH,"//*[@id='FlightSearchForm_ROUND_TRIP']").clear()
# driver.find_element(By.XPATH,"//*[@id='FlightSearchForm_ROUND_TRIP']").send_keys("May 11 - May 18")
#
# driver.find_elements("search_button").click()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.expedia.com/")
#
# time.sleep(3)
#
# links=driver.find_elements(By.TAG_NAME,"a")
#
# print("This page has this number of links:",len(links))
#
# for link in links:
#     print(link.text)
#
# driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.timesofindia.com")
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='root']/div/header/nav/ul[1]/li[1]/button").click()
# # driver.find_element()
# # driver.switch_to.alert.dismiss()
# print(driver.title)

# element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/header/nav/ul[1]/li[1]/button"))
# )
# element.click()

driver.maximize_window()
time.sleep(10)
# driver.execute_script("window.scrollBy(0,5000)","")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)


