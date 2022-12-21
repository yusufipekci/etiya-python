# bir kütüphaneden dosya import etmek
# kalıp => from {kütüphane-ismi} import {nesne-ismi}
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# HTML Locators

driver = webdriver.Chrome()
driver.get("https://tr-tr.facebook.com/")  # chromeda bu linki aç
# driver.maximize_window() #Ekranı tam boyuta getirir
# sitenin açılmasını bekle!
sleep(3) # defensive programming
input = driver.find_element(By.NAME,"email") # inputu bul
input.send_keys("yusufipekcii")
input = driver.find_element(By.NAME,"pass")
input.send_keys("123456789")
login = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
loginText = login.text
login.click()
sleep(3)
asilBaslik=driver.title
if  asilBaslik=="Facebook":
    print("Giriş başarılı")
else:
    print("Giriş başarısız!")
sleep(5)
