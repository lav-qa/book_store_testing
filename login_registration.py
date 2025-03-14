import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

#Implicit wait
driver.implicitly_wait(5)
### registration
# account data
test_email = 'test_mail@gmail.com'
password = '2miVeZkZjABm'
# open link
driver.get("https://practice.automationtesting.in/")
# go to My account and enter the data for registration
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
email_reg = driver.find_element_by_css_selector("[id='reg_email']")
email_reg.send_keys(test_email)
password_reg = driver.find_element_by_css_selector("[id='reg_password']")
password_reg.send_keys(password)

#submit registration
# time before register button become available always is different - 2min should be enough
reg_btn = WebDriverWait(driver,120).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"[name='register']")))
reg_btn.click()
time.sleep(5)
driver.quit()

### login
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
#Implicit wait
driver.implicitly_wait(5)
# open link
driver.get("https://practice.automationtesting.in/")
# go to My account and enter the data for login
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
email_log = driver.find_element_by_css_selector("[id='username']")
email_log.send_keys(test_email)
password_log = driver.find_element_by_css_selector("[id='password']")
password_log.send_keys(password)
#submit login
login_btn = driver.find_element_by_css_selector("[name='login']")
login_btn.click()
# checking logout button
logout_btn = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-MyAccount-navigation-link--customer-logout")))
print("Logout element is found")
time.sleep(5)

driver.quit()
