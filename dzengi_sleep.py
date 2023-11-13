import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.maximize_window()
time.sleep(1)

driver.get("https://dzengi.com")
time.sleep(5)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже

# Найдем кнопку, которая отправляет введенное решение
login_button_min = driver.find_element(By.CSS_SELECTOR, "[aria-label='Log In']")
login_button_min.click()
time.sleep(5)

#Заполняем форму: LOGIN
user_name = driver.find_element(By.NAME, 'email')
user_name.send_keys("hello1@hello.com")
time.sleep(2)

#Вводим пароль
password = driver.find_element(By.NAME, 'password')
password.send_keys("QqПривет1!")
time.sleep(2)

#Нажимаем кнопку Отправить
signin_button = driver.find_element(By.CLASS_NAME, "l_btn")
signin_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
