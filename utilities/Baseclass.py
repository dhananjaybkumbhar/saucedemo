from selenium.webdriver.common.by import By


def selenium():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from time import sleep
    global driver
    driver=webdriver.Chrome()
    driver.get('https://www.saucedemo.com')


selenium()


def username():
    driver.find_element(By.ID,'user-name')

def password():
    driver.find_element(By.ID,'password')

def login_btn():
    driver.find_element(By.ID,'login-button')