import time

import openpyxl
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()




driver.get('https://www.saucedemo.com/')


def test_S_Cart_01():
    driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(2)
    driver.find_element(By.ID,'login-button').click()
    time.sleep(15)
    cart=driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').is_displayed()
    assert cart

def test_S_Cart_02():
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(2)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(15)
    cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').is_enabled()
    assert cart

def test_S_Cart_03():
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(2)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(15)
    driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    cart = driver.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a').text
    assert cart=='1'

def test_S_Cart_04():
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(2)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').text
    assert cart == '1'
    driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').text
    assert cart =='2'

def test_S_Cart_06():
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(2)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').text
    assert cart == '1'
    driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]').click()




















