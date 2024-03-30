from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest


class Test_Sauce: 

    def setup_method(self):
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")  
    
    def teardown_method(self):
        self.driver.quit()

    def test_invalid_login(self): 
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(By.ID,"user-name"))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(By.ID,"password"))
                                                 
        actions = ActionChains(self.driver)                                                 
        actions.send_keys_to_element(userNameInput,"1")
        actions.send_keys_to_element(passwordInput,"1")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(By.ID,"login-button"))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        assert errorMessage.text == "ERROR!!! Epic sadface: Username and password do not match any user in this service"
     

    def test_null_username(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(By.ID,"user-name"))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(By.ID,"password"))
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(By.ID,"login-button"))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"")
        #actions.send_keys_to_element(passwordInput,"")
        actions.click(loginButton)
        actions.perform()
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        assert errorMessage == "Epic sadface: Username is required"
        
        

    def test_null_password(self):
        
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Password is required"
        print(f"Epic sadface: Password is required uyarı mesajı gösterilmiştir = {testResult}")
        

    def test_user_locked(self):
        driver = self.precondition()
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("locked_out_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        expectedMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = expectedMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Epic sadface: Sorry, this user has been locked out. uyarı mesajı gösterilmiştir = {testResult}")
        

    def test_products_list(self):
        driver = self.precondition()
        userNameInput = driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)
        productList = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün sayısı {len(productList)} adettir.")
           

testClass = Test_Sauce()
testClass.test_products_list()
testClass.test_user_locked()
testClass.test_null_password()
testClass.test_null_value()
testClass.test_invalid_login()





