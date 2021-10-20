from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://oxylabs.io/blog')
blog_titles = driver.find_elements_by_css_selector(".blog-card__content-title")
for title in blog_tiles:
    print(title.text)
driver.quit() # closing the browser