from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Define Service Options
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Load the web page
driver.get('https://demoqa.com/login')

# Load username , password and Login Button
#username_field = WebDriverWait(driver,7).until(EC.visibility_of_element_located((By.ID,'userName')))
#password_field = WebDriverWait(driver,7).until(EC.visibility_of_element_located((By.ID,'password')))
username_field = driver.find_element(By.ID,'userName')
password_field = driver.find_element(By.ID,'password')
login_button = driver.find_element(By.ID,'login')



# Fill in username and password  and click login button
username_field.send_keys('azvikash')
password_field.send_keys('Python@123')
driver.execute_script('arguments[0].click()',login_button)


# Locate element dropdown and textbox
element = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')
#elements = (WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
driver.execute_script('arguments[0].click()',element)

textbox = driver.find_element(By.XPATH,'//*[@id="item-0"]/span')
driver.execute_script('arguments[0].click()',textbox)

# Locate the form fields
textbox_name = driver.find_element(By.ID,"userName")
textbox_email = driver.find_element(By.ID,"userEmail")
textbox_cur_address = driver.find_element(By.ID,"currentAddress")
textbox_per_address = driver.find_element(By.ID,"permanentAddress")

# Send data to form fields
textbox_name.send_keys('Phani Vikash')
textbox_email.send_keys('PhaniVikash@gmail.com')
textbox_cur_address.send_keys('Vijayawada')
textbox_per_address.send_keys('America')

# Submit
textbox_submit = driver.find_element(By.ID,"submit")
driver.execute_script('arguments[0].click()',textbox_submit)


upload_download = driver.find_element(By.ID,"item-7")
driver.execute_script('arguments[0].click()',upload_download)
upload_download_button = driver.find_element(By.ID,"downloadButton")
driver.execute_script('arguments[0].click()',upload_download_button)




a=int(input("Press any number to exit :"))
if a >= 0:
    exit()

driver.quit()