from selenium.webdriver import Chrome
driver = Chrome(executable_path='D:/Dev_Tool/ChromeDriver/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
blog_titles = driver.get_elements_by_css_selector(' h2.blog-card__content-title')
for title in blog_tiles:
    print(title.text)
driver.quit() # closing the browser