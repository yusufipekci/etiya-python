from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.kodlama.io/")
driver.maximize_window()

courses = driver.find_elements(By.XPATH,"//*[@class='course-box-image-container']")
numberofcourses = len(courses)

if numberofcourses == 6:
    print("Kurs sayısı doğru!", "Kurs Sayısı:" + str(numberofcourses))
else:
    print("Kurs sayısı yanlış!")
driver.execute_script("window.scroll(0,200)")
driver.save_screenshot(str(date.today()) + '(1).png')
sleep(3)

search = driver.find_element(By.NAME,"query")
search.send_keys("Senior Ya")
sleep(3)
findTitle = driver.find_element(By.XPATH,'//*[@title="Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)"]')
titleCorrection = findTitle.text
sleep(2)

if titleCorrection == "Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)":
    print("Kurs ismi doğru!")
else:
    print("Kurs ismi yanlış!")
driver.save_screenshot(str(date.today()) + '(2).png')
