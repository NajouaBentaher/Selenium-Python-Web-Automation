from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# create the browser instance
"browser = webdriver.Firefox('geckodriver.exe')"
browser = webdriver.Chrome()
sleep(1)

browser.maximize_window()
sleep(1)

browser.get('https://www.saucedemo.com/')
sleep(1)

# login process

username_input = browser.find_element(By.NAME, 'user-name')
sleep(1)

username_input.send_keys('standard_user')

password_input = browser.find_element(By.NAME, 'password')
sleep(1)

password_input.send_keys('secret_sauce')

login_button = browser.find_element(By.NAME, 'login-button').click()


# add to cart process

item1 = browser.find_element(By.CLASS_NAME, 'inventory_item_name').click()
sleep(3)

add_to_cart1 = browser.find_element(By.NAME, 'add-to-cart').click()
sleep(1)

back = browser.find_element(By.NAME, 'back-to-products').click()
sleep(1)

add_to_cart2 = browser.find_element(By.NAME, 'add-to-cart-sauce-labs-bike-light').click()
sleep(1)

add_to_cart3 = browser.find_element(By.NAME, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
sleep(1)

# cart and checkout

cart = browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
sleep(1)

# scroll

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(2)

checkout = browser.find_element(By.NAME, 'checkout').click()
sleep(3)

# logout

menu = browser.find_element(By.ID, 'react-burger-menu-btn').click()
sleep(1)

logout = browser.find_element(By.ID, 'logout_sidebar_link').click()
sleep(2)

browser.quit()










