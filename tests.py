from selenium import webdriver



from unittest import TestCase

from selenium.webdriver.common.by import By


class Test(TestCase):
    def test_title_name(self):
        chromedriver = "chromedriver"
        driver = webdriver.Chrome(chromedriver)
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/')
        self.assertEqual('APPSTRACTED',driver.title,'Test Title!')

    def test_admin_login(self):
        chromedriver = "chromedriver"
        driver = webdriver.Chrome(chromedriver)
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/adminlogin')

        username = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        password = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        username.send_keys("admin")
        password.send_keys("admin")
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        self.assertEqual('http://127.0.0.1:8000/adminpanel/', driver.current_url, 'Test Admin Login!')

    def test_contact_form(self):
        chromedriver = "chromedriver"
        driver = webdriver.Chrome(chromedriver)
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/contact')

        customername = driver.find_element(By.CSS_SELECTOR, 'input[name="customername"]')
        customeremail = driver.find_element(By.CSS_SELECTOR, 'input[name="customeremail"]')
        customermessage = driver.find_element(By.CSS_SELECTOR, 'input[name="customermessage"]')

        customername.send_keys("test")
        customeremail.send_keys("test@gmail.com")
        customermessage.send_keys("test my test")

        submit_button = driver.find_element(By.CLASS_NAME,"v3_5595")
        submit_button.click()

