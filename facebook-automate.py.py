from selenium import webdriver
import time
username= "9845404532"
user_password= "****************"

url = "https://facebook.com"

driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Documents\\chromedriver_win32 (1)\\chromedriver.exe")

driver.get(url)

email_input = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
login_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")

email_input.send_keys(username)
password.send_keys(user_password)
login_btn.click()
time.sleep(30)
