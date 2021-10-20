from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.python.org")

search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with Selenium")
search_bar.send_keys(Keys.RETURN)

print(driver.current_url)
print(driver.window_handles)
driver.close()