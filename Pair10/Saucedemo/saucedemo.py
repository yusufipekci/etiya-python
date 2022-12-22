from datetime import date
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pathlib import Path
from constants2 import *

class Test_odev3:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_DOMAIN_URL)

    def teardown_method(self):
        self.driver.quit()

#-Doğru bilgilerden standard_user kullanıcı adıyla giriş yapılmanın doğru olup olmadığı kontrol edilmelidir.

    def test_Giris(self):
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,USER_NAME_ID)))
        UserName = self.driver.find_element(By.ID,USER_NAME_ID)
        UserName.send_keys("standard_user")
      
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,PASSWORD_ID)))
        PasswordName= self.driver.find_element(By.ID,PASSWORD_ID)
        PasswordName.send_keys("secret_sauce")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,LOGIN_ID)))
        LoginBtn= self.driver.find_element(By.ID,LOGIN_ID)
        LoginBtn.click()

        Giristitle= self.driver.find_element(By.XPATH,GIRIS_TITLE_XPATH)
        GiristitleText=Giristitle.text
        assert GiristitleText =="PRODUCTS"

#-Yanlış bilgiler girildiğinde uyarı çıkıp çıkmadığı test edilmelidir.

    def test_YanlisGiris(self):
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,USER_NAME_ID)))
        UserName = self.driver.find_element(By.ID,USER_NAME_ID)
        UserName.send_keys("standard ")
      
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,PASSWORD_ID)))
        PasswordName= self.driver.find_element(By.ID,PASSWORD_ID)
        PasswordName.send_keys("secret ")

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,LOGIN_ID)))
        LoginBtn= self.driver.find_element(By.ID,LOGIN_ID)
        LoginBtn.click()
        ErrorMessage = self.driver.find_element(By.CLASS_NAME, ERROR_MSJ)
        ErrorMsjText=ErrorMessage.text 
        assert  ErrorMsjText is not None
#-Yanlış bilgiler girildiğinde çıkan uyarı mesajının doğruluğu kontrol edilmelidir 
# Epic sadface: Username and password do not match any user in this service

    def test_UyariMesajKontrol(self):
        
        self.test_YanlisGiris()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,LOGIN_ID)))
        ErrorMessage = self.driver.find_element(By.CLASS_NAME, ERROR_MSJ)
        ErrorMsjText=ErrorMessage.text 
        assert ErrorMsjText =="Epic sadface: Username and password do not match any user in this service"

#-Ana sayfada 6 adet ürün listelendiği kontrol edilmelidir.
    def test_product_list(self):

        self.test_Giris()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, PRODUCTNUMBER)))
        products = self.driver.find_elements(By.CLASS_NAME, PRODUCTNUMBER)
        numberOfProducts = len(products)
        assert numberOfProducts == 6

#-Sepete Ekle butonuna tıklandığında butonun texti REMOVE olmalıdır.    
    def test_ButonKontrol(self):
        self.test_Giris()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, BUTTONNAME)))
        AddtoCard = self.driver.find_element(By.NAME, BUTTONNAME)
        AddtoCard.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, REMOVEBTNNAME)))
        Remove=self.driver.find_element(By.NAME, REMOVEBTNNAME)
        RemoveText=Remove.text

        assert RemoveText=="REMOVE"

#-Sepete 1 adet ürün eklendiğinde sağ üstteki sepet üzerinden 1 sayısı çıkmalıdır.

    def test_BasketKontrol(self):
        self.test_Giris()  
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, BUTTONNAME)))
        AddtoCard = self.driver.find_element(By.NAME, BUTTONNAME)
        AddtoCard.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, BASKETID)))
        Basket = self.driver.find_element(By.ID, BASKETID)
        BasketText=Basket.text

        assert BasketText==BASKETIDTEXT





      