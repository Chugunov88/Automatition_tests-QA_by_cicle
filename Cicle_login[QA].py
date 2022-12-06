from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



"""Открыть наш линк, ввести логин пароль и залогиниться"""
driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\python_selenium\\chromedriver.exe')
base_url = 'https://saucedemo.com/'
driver.get(base_url)

user_list = ["standard_user", "locked_out_user", "performance_glitch_user", "problem_user"]
#                    0               1                    2                      3
password_all = "secret_sauce"

for i in user_list:
    print("Test Start" + "-" + i)
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    user_name.send_keys(i)
    print("Input login")
    password = driver.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys(password_all)
    print("Input Password")


    button_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
    button_login.click()
    try:
        warring_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')))
        value_warring_text = warring_text.text
        print(value_warring_text)
        print("Test " + i + " " + "Passed with Error, Continue")
    except TimeoutException as exception:
        print("Login Success")


    """Убедиться что вошёл в аккаунт и выйти"""
    try:
        success_test = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
        value_success_test = success_test.text
        assert value_success_test == 'PRODUCTS'
        print("Test Passed" + "-" + i)
    except:
        driver.refresh()
        continue

    """Логуат при помощи кнопки из бургер меню"""
    burger_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
    burger_menu.click()
    log_out = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
    log_out.click()
print("All tests have been completed!!!")