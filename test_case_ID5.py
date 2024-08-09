from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome()

try:
    driver.get('http://www.saucedemo.com')
    wait = WebDriverWait(driver, 10)
    wait.until(lambda x: driver.find_element(by=By.ID, value='user-name').is_displayed)
    username_box = driver.find_element(By.ID, 'user-name')
    password_box = driver.find_element(By.ID, 'password')
        
    username_box.send_keys('standard_user')
    password_box.send_keys('secret_sauce')

    login = driver.find_element(By.CSS_SELECTOR, '.btn_action')
    login.click()
    time.sleep(5)

    select_item=driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
    select_item.click()
    time.sleep(5)

    bucket=driver.find_element(By.ID,"shopping_cart_container")
    bucket.click()
    time.sleep(5)

    remove_item=driver.find_element(By.ID,"remove-sauce-labs-backpack")
    remove_item.click()
    time.sleep(5)

    assert "/inventory.html" in driver.current_url
finally:
    driver.quit()