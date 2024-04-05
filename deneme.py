from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class test_Sauce:
    def onkosul (self):
        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        return driver #driveri döndür.

    def bosgiris (self):
        driver= self.onkosul() #driveri çağırdık.
        sleep (5)
        loginButton=driver.find_element(By.ID,"login-button") # find elemnt: elementi bul, by: neyinden
        sleep (5)
        loginButton.click()
        erorMesaji=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3") #eror mesajını bulduk.
        testResult = erorMesaji.text ==  "Epic sadface: Username is required" #eror msajının verilene eşitmi bakalıcak
        sleep(5)
        print(f"Test Sonucu:{testResult}") 


# def sifrebos (self):
#     driver= self.onkosul()
#     kullaniciAdi=driver.find_element(By.ID,"user-name").send_keys(kullaniciAdi,"gnc")


testClass=test_Sauce() # classı değişkene atıyoruz.
testClass.onkosul() # değişkenle fonksiyonu çalıştırıyoruz.
testClass.bosgiris() #değişkenle bosgirişi çalıştır.