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
    users_list=["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_userone"]

    for user in users_list:
        username_box = driver.find_element(By.ID, 'user-name')
        password_box = driver.find_element(By.ID, 'password')
        
        username_box.send_keys(user)
        password_box.send_keys('secret_sauce')

        login = driver.find_element(By.CSS_SELECTOR, '.btn_action')
        login.click()
        time.sleep(5)

        icon= driver.find_element(By.ID,"react-burger-menu-btn")
        icon.click()
        time.sleep(5)
        logout= driver.find_element(By.ID, "logout_sidebar_link")
        logout.click()
        time.sleep(5)
        print(user)
    assert "/inventory.html" in driver.current_url
finally:
    driver.quit()