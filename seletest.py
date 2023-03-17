from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
import time


opts = ChromeOptions() 
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)

driver.get("https://kejar.id/login")

# log
driver.find_element(by=By.NAME, value="username").send_keys("arfanhash659") # Ganti ini ke user sendiri
driver.find_element(by=By.NAME, value="password").send_keys("arfanhash0764") # Ganti ini ke pass nya
driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/form/button').click()

# Ke Bkp
driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[4]/div[4]/a[2]').click()
driver.refresh()
time.sleep(5) 

# Looping ke minggu ke 20
for i in range(9):
    driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[2]/button[1]').click()
    time.sleep(6)
    


# Start
driver.find_element(By.XPATH,'/html/body/div[4]/div[6]/div[2]/table/tbody[1]/tr[2]/td[5]').click()


# Shalat malam
driver.find_element(By.XPATH,f'/html/body/div[18]/div/div/div/div[2]/div/form[1]/div[2]/div[4]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[2]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[3]/div[2]/div[5]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[4]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,'//*[@id="btn-success"]/button').click()
time.sleep(1) 

# Subuh
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[1]/div[2]/div[2]/label').click() # salat subuh, qobliyah
driver.find_element(By.XPATH,'//*[@id="modal-content-habbit"]/form[2]/div/div[2]/label').click()        
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[3]/div/div[4]/label').click()    
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[4]/div/div[3]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[5]/div/div[3]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[6]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,'//*[@id="btn-success"]/button').click()
time.sleep(1)
    
# Zikir pagi
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form/div[2]/div[3]/label').click() # zikir pagi
driver.find_element(By.XPATH,'/html/body/div[19]/div/div/div/div[3]/div/button').click()
time.sleep(1)
    
# Duha
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[1]/div[2]/div[2]/label').click() # salat duha
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[2]/div[2]/div[1]/label').click() 
driver.find_element(By.XPATH,'//*[@id="btn-success"]/button').click()
time.sleep(1)
    
# Dzuhur
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[1]/div[2]/div[2]/label').click() # salat zuhur 
driver.find_element(By.XPATH,'//*[@id="modal-content-habbit"]/form[2]/div/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[3]/div/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[4]/div/div[3]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[5]/div/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[6]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[7]/div[2]/div[2]/label').click() 
driver.find_element(By.XPATH,'//*[@id="btn-success"]/button').click()
time.sleep(1)
    
# Ashar
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[1]/div/div[2]/label').click() # salat asar
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[2]/div/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[3]/div/div[3]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[4]/div/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[5]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,'//*[@id="btn-success"]/button').click()
time.sleep(1)
    
# Zikir sore
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form/div[2]/div[3]/label').click() # zikir sore
driver.find_element(By.XPATH,'//*[@id="btn-success"]/button').click()
time.sleep(1)
    
# Maghrib
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[1]/div[2]/div[2/label').click() #salat maghrib
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[2]/div/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[3]/div/div[4]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[4]/div/div[3]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[5]/div/div[3]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[6]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[7]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,'//*[@id="btn-success"]/button').click()
time.sleep(1)
    
# Isya
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[1]/div[2]/div[2]/label').click() # salat isya
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[2]/div/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[3]/div/div[4]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[4]/div/div[3]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[5]/div/div[3]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[6]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,f'//*[@id="modal-content-habbit"]/form[7]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,'//*[@id="btn-success"]/button').click()
time.sleep(1)
    
# Kesehatan
driver.find_element(By.XPATH,f'/html/body/div[18]/div/div/div/div[2]/form[1]/div[2]/div[1/label').click() # olahraga dan tidur
driver.find_element(By.XPATH,f'/html/body/div[18]/div/div/div/div[2]/form[2]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH,'/html/body/div[18]/div/div/div/div[3]/button[2]').click()
time.sleep(1)
    
# Tumbler
driver.find_element(By.XPATH,'/html/body/div[19]/div/div/div/div[2]/form/div[2]/div[1]/label').click()
driver.find_element(By.XPATH,'/html/body/div[19]/div/div/div/div[3]/button[2]/span').click()
time.sleep(1)

    





 
    
