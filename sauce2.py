from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3") #tek tırnağa çevirdik yine. hatalı giriş yapıp hata mesajının xpathini aldık
        #print(errorMessage.text)
        testResult = errorMessage.text == "ERROR!!! Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")

testClass = Test_Sauce() #classları kendi başına çalıştıramadığımız için onu değişkene atıyoruz
testClass.test_invalid_login()



