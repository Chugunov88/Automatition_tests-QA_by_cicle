import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


print("Приветствую тебя в нашем магазине")
print("Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")
i = int(input())
print(i)
if i == 1:
    product = '4'
    print(product)
elif i == 2:
    product = '0'
    print(product)
elif i == 3:
    product = '1'
    print(product)
elif i == 4:
    product = '5'
    print(product)
elif i == 5:
    product = '2'
    print(product)
elif i == 6:
    product = '3'
    print(product)
else:
    print("Неверный номер товара")
    quit()


"""Открыть наш линк, ввести логин пароль и залогиниться"""
driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\python_selenium\\chromedriver.exe')
base_url = 'https://saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
time.sleep(2)
user_name.send_keys(login_standard_user)
print("Input login")
time.sleep(2)
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
time.sleep(1)
button_login.click()
print("Click Login Button")

"""Уникальный локатор название товара"""
locator = "item_" + product + "_title_link"
print(locator)

any_product = driver.find_element(By.XPATH, '//a[@id="{0}"]'.format(locator))
value_any_product = any_product.text
print(value_any_product)


"""Уникальный Локатор цены"""
price_locator = 'div/div[' + str(i) + ']/div[2]/div[2]/div'
print(price_locator)

any_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div/{0}'.format(price_locator))
value_any_price = any_price.text
print(value_any_price)

"""Название товара заменить пробелы на тире и сделать все буквы маленькими"""
value_any_productX = any_product.text
print(value_any_productX)
l = value_any_productX.split()
s1 = '-'.join(l)
print(s1)

s1b = 'add-to-cart-' + s1
s1bl = s1b.lower()      #делает все буквы маленькими
print(s1bl)

any_product_button_locator = driver.find_element(By.XPATH, "//button[@id='{0}']".format(s1bl))
time.sleep(2)
any_product_button_locator.click()

"""Кликнуть на корзину"""
checkout = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
time.sleep(2)
checkout.click()
print("Enter Cart")

"""INFO Cart Product"""
cart_product = driver.find_element(By.XPATH, '//a[@id="{0}"]'.format(locator))
value_cart_product = cart_product.text
print(value_cart_product)
assert value_any_product == value_cart_product
print("Название товара верно")

price_cart_product = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_product = price_cart_product.text
print(value_cart_product)

assert value_any_price == value_cart_product
print("Цена товара верна")

checkout_confirm = driver.find_element(By.XPATH, '//button[@class="btn btn_action btn_medium checkout_button"]')
time.sleep(2)
checkout_confirm.click()
print("Click Checkout")

"""Select User INFO"""
print('CHECKOUT: YOUR INFORMATION')
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.click()
time.sleep(2)
first_name.send_keys('Ivan')
last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.click()
time.sleep(2)
last_name.send_keys('Chugunov')
postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
postal_code.click()
time.sleep(2)
postal_code.send_keys(428030)
checkout_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
time.sleep(2)
checkout_continue.click()
print("Add holder info")

"""Финальное сравнение цены и товара"""
finish_product = driver.find_element(By.XPATH, '//a[@id="{0}"]'.format(locator))
value_finish_product = finish_product.text
print(value_finish_product)
assert value_any_product == value_finish_product
print("Финальное название товара верно")

price_finish_product = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_finish_product = price_finish_product.text
print(value_price_finish_product)

assert value_price_finish_product == value_cart_product
print("Финальная Цена  товара верна")


"""Последний штрих"""
summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')  # Item total
value_summary_price = summary_price.text
print(value_summary_price)
#
"""Изъятие числа"""
str1 = value_summary_price
DONE1 = float((str1.translate({ord(i): None for i in 'Item total: ,$'})))
print(DONE1) # Item total
#
"""Сравнение суммы товаров с нашей конечной суммой"""

str2 = value_cart_product
DONE2 = float((str2.translate({ord(i): None for i in '$'})))
print(DONE2)  #ранняя цена товара в корзине

assert DONE1 == DONE2
print("Цена товаров соответствует")

Done = driver.find_element(By.XPATH, '//*[@id="finish"]')
time.sleep(2)
Done.click()
print('Well Done')


