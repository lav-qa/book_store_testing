import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

# account data
test_email = 'test_mail@gmail.com'
password = '2miVeZkZjABm'

### TEST 1
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# #Implicit wait
# driver.implicitly_wait(5)
# # open link
# driver.get("https://practice.automationtesting.in/")
# # go to My account and enter the data for login
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# email_log = driver.find_element_by_css_selector("[id='username']")
# email_log.send_keys(test_email)
# password_log = driver.find_element_by_css_selector("[id='password']")
# password_log.send_keys(password)
# #submit login
# login_btn = driver.find_element_by_css_selector("[name='login']")
# login_btn.click()
# #go to shop
# go2shop = driver.find_element_by_link_text("Shop")
# go2shop.click()
# #open book "HTML 5 Forms"
# html5 = driver.find_element_by_css_selector(".products .post-181 h3")
# html5.click()
# #checking the title "HTML5 Forms"
# book_title = driver.find_element_by_css_selector("h1.product_title")
# title = book_title.text
# assert title == "HTML5 Forms"
#
# driver.quit()
#
# ### TEST 2
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# #Implicit wait
# driver.implicitly_wait(5)
# # open link
# driver.get("https://practice.automationtesting.in/")
# # go to My account and enter the data for login
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# email_log = driver.find_element_by_css_selector("[id='username']")
# email_log.send_keys(test_email)
# password_log = driver.find_element_by_css_selector("[id='password']")
# password_log.send_keys(password)
# #submit login
# login_btn = driver.find_element_by_css_selector("[name='login']")
# login_btn.click()
# #go to shop
# go2shop = driver.find_element_by_link_text("Shop")
# go2shop.click()
# #open section HTML
# html_section = driver.find_element_by_link_text("HTML")
# html_section.click()
# # check the number of items
# html_books = driver.find_elements_by_css_selector("ul.products.masonry-done li")
# assert len(html_books) == 3
# driver.quit()

# ### TEST 3
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# #Implicit wait
# driver.implicitly_wait(5)
# # open link
# driver.get("https://practice.automationtesting.in/")
# # go to My account and enter the data for login
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# email_log = driver.find_element_by_css_selector("[id='username']")
# email_log.send_keys(test_email)
# password_log = driver.find_element_by_css_selector("[id='password']")
# password_log.send_keys(password)
# #submit login
# login_btn = driver.find_element_by_css_selector("[name='login']")
# login_btn.click()
# #go to shop
# go2shop = driver.find_element_by_link_text("Shop")
# go2shop.click()
# #check default sorting
# selected_option = driver.find_element_by_css_selector("select.orderby option[selected]")
# option_check = selected_option.get_attribute("value")
# assert option_check == "menu_order"
# # sort by price
# select_field = driver.find_element_by_css_selector("select.orderby")
# selector = Select(select_field)
# selector.select_by_value("price-desc")
# #check sort by price desc
# selected_price_option = driver.find_element_by_css_selector("select.orderby option[selected]")
# option_check = selected_price_option.get_attribute("value")
# assert option_check == "price-desc"
# driver.quit()

# ### TEST 4
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# #Implicit wait
# driver.implicitly_wait(5)
# # open link
# driver.get("https://practice.automationtesting.in/")
# # go to My account and enter the data for login
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# email_log = driver.find_element_by_css_selector("[id='username']")
# email_log.send_keys(test_email)
# password_log = driver.find_element_by_css_selector("[id='password']")
# password_log.send_keys(password)
# #submit login
# login_btn = driver.find_element_by_css_selector("[name='login']")
# login_btn.click()
# #go to shop
# go2shop = driver.find_element_by_link_text("Shop")
# go2shop.click()
# # open book "Android Quick Start Guide"
# android_book = driver.find_element_by_css_selector(".products .post-169 h3")
# android_book.click()
# #check old price
# old_price = driver.find_element_by_css_selector(".price del .amount")
# old_price_amount = old_price.text
# assert old_price_amount == "₹600.00"
# #check new price
# new_price = driver.find_element_by_css_selector(".price ins .amount")
# new_price_amount = new_price.text
# assert new_price_amount == "₹450.00"
# # Explicit wait + click book image
# view_image = WebDriverWait(driver,20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images a")))
# view_image.click()
# # Explicit wait + close image
# close_image = WebDriverWait(driver,20).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "pp_close")))
# close_image.click()
# driver.quit()

# ### TEST 5
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# #Implicit wait
# driver.implicitly_wait(5)
# # open link
# driver.get("https://practice.automationtesting.in/")
# #go to shop
# go2shop = driver.find_element_by_link_text("Shop")
# go2shop.click()
# # add book "HTML5 WebApp Development" to cart
# add_to_basket = driver.find_element_by_css_selector("[data-product_id = '182']")
# add_to_basket.click()
# # check cart data
# time.sleep(5) # time for the data to update
# items_in_cart = driver.find_element_by_class_name("cartcontents")
# number_items = items_in_cart.text
# assert number_items == "1 Item"
# cart_amount = driver.find_element_by_css_selector("a.wpmenucart-contents .amount")
# amount = cart_amount.text
# assert amount == "₹180.00"
# # go to cart
# go2cart = driver.find_element_by_class_name("wpmenucart-contents ")
# go2cart.click()
# #Explicit wait  + subtotal check
# subtotal = WebDriverWait(driver,10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-title='Subtotal']"))).text
# print(subtotal)
# #Explicit wait + total check
# total = WebDriverWait(driver,10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-total [data-title='Total']"))).text
# print(total)
# driver.quit()

# ### TEST 6
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# #Implicit wait
# driver.implicitly_wait(5)
# # open link
# driver.get("https://practice.automationtesting.in/")
# #go to shop
# go2shop = driver.find_element_by_link_text("Shop")
# go2shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# # add 2 books to cart "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# html5 = driver.find_element_by_css_selector("ul.products [data-product_id='182']")
# html5.click()
# time.sleep(5)
# js_data = driver.find_element_by_css_selector("ul.products [data-product_id='180']")
# js_data.click()
# # go to cart
# go2cart = driver.find_element_by_class_name("wpmenucart-contents")
# go2cart.click()
# #delete first book and undo
# time.sleep(5)
# remove_html5 = driver.find_element_by_css_selector("a.remove[data-product_id='182']")
# remove_html5.click()
# undo = driver.find_element_by_css_selector(".woocommerce-message a")
# undo.click()
# #change quantity
# qty_field = driver.find_element_by_css_selector("tr.cart_item:nth-child(1) input.qty")
# qty_field.clear()
# qty_field.send_keys("3")
# #update cart
# upd_btn = driver.find_element_by_css_selector("input[name='update_cart']")
# upd_btn.click()
# # check quantity
# qty_field = driver.find_element_by_css_selector("tr.cart_item:nth-child(1) input.qty")
# qty_val = qty_field.get_attribute("value")
# assert qty_val == "3"
# #apply coupon
# time.sleep(5)
# coupon_btn = driver.find_element_by_css_selector("input[name='apply_coupon']")
# coupon_btn.click()
# #check message
# error_message = WebDriverWait(driver,10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error li"), "Please enter a coupon code."))
#
# driver.quit()


### TEST 7
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
#Implicit wait
driver.implicitly_wait(5)
# open link
driver.get("https://practice.automationtesting.in/")
#go to shop
go2shop = driver.find_element_by_link_text("Shop")
go2shop.click()
driver.execute_script("window.scrollBy(0, 300);")
# add book to cart "HTML5 WebApp Development"
html5 = driver.find_element_by_css_selector("ul.products [data-product_id='182']")
html5.click()
time.sleep(5)
#  go to cart
go2cart = driver.find_element_by_class_name("wpmenucart-contents")
go2cart.click()
# explicit wait + click proceed to checkout
checkout_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()
# fill necessary fields
first_name = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"billing_first_name")))
first_name.send_keys("Test")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("User")
email_field = driver.find_element_by_id("billing_email")
email_field.send_keys(test_email)
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("111111111")
country_selector = driver.find_element_by_id("s2id_billing_country")
country_selector.click()
country_input = driver.find_element_by_id("s2id_autogen1_search")
country_input.send_keys("Russia")
first_match = driver.find_element_by_css_selector("ul.select2-results li:nth-child(1) div")
first_match.click()
street_address = driver.find_element_by_id("billing_address_1")
street_address.send_keys("Testing address 1")
city = driver.find_element_by_id("billing_city")
city.send_keys("Moscow")
state = driver.find_element_by_id("billing_state")
state.send_keys("Russia")
post_code = driver.find_element_by_id("billing_postcode")
post_code.send_keys("111111")
# choose payment
driver.execute_script("window.scrollBy(0,300);")
time.sleep(5)
check_pay_radio = driver.find_element_by_css_selector(".input-radio[value='cheque']")
check_pay_radio.click()
# click place order
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
# checking "Thank you. Your order has been received."
successful_order = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.woocommerce p:nth-child(1)"),"Thank you. Your order has been received."))
# checking "Check Payments" in payment method
payment_check = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,"tfoot tr:nth-child(3)"), "Check Payments"))
time.sleep(5)
driver.quit()
