from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://oxylabs.io/blog')
blog_titles = driver.find_element_by_css_selector("h2.blog-card__content-title")
#for title in blog_tiles:
print(blog_titles.text)
#driver.quit() # closing the browser