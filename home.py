import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

#Implicit wait
driver.implicitly_wait(5)
# open link and scrolling window
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
#open book's page
selenium_ruby = driver.find_element_by_css_selector(".product_tag-ruby h3")
selenium_ruby.click()
#go to reviews and leave a test-comment
reviews = driver.find_element_by_css_selector(".reviews_tab a")
reviews.click()
stars_5 = driver.find_element_by_css_selector("p.stars a.star-5")
stars_5.click()
comment = driver.find_element_by_css_selector("[id='comment']")
comment.send_keys("Nice book!")
test_name = driver.find_element_by_css_selector("[id='author']")
test_name.send_keys("test")
email_test = driver.find_element_by_css_selector("[id='email']")
email_test.send_keys("testing_mail@gmail.com")
submit_btn = driver.find_element_by_css_selector("[id='submit']")
submit_btn.click()
time.sleep(5)
driver.quit()