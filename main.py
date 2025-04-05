from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebAutomation:
    def __init__(self):
        # Define Service Options
        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def login(self,username,password):
        # Load the web page
        self.driver.get('https://demoqa.com/login')

        # Load username , password and Login Button
        #username_field = WebDriverWait(driver,7).until(EC.visibility_of_element_located((By.ID,'userName')))
        #password_field = WebDriverWait(driver,7).until(EC.visibility_of_element_located((By.ID,'password')))
        username_field = self.driver.find_element(By.ID,'userName')
        password_field = self.driver.find_element(By.ID,'password')
        login_button = self.driver.find_element(By.ID,'login')


        # Fill in username and password  and click login button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script('arguments[0].click()',login_button)
                                                                                                                

    def fill_form(self,name,email,cur_add,per_add):

        # Locate element dropdown and textbox
        element = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')
        #elements = (WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]
        # /div/div/div/div[1]/div/div/div[1]/span/div'))))
        self.driver.execute_script('arguments[0].click()',element)

        textbox = self.driver.find_element(By.XPATH,'//*[@id="item-0"]/span')
        self.driver.execute_script('arguments[0].click()',textbox)

        # Locate the form fields
        textbox_name = self.driver.find_element(By.ID,"userName")
        textbox_email = self.driver.find_element(By.ID,"userEmail")
        textbox_cur_address = self.driver.find_element(By.ID,"currentAddress")
        textbox_per_address = self.driver.find_element(By.ID,"permanentAddress")

        # Send data to form fields
        textbox_name.send_keys(name)
        textbox_email.send_keys(email)
        textbox_cur_address.send_keys(cur_add)
        textbox_per_address.send_keys(per_add)

        # Submit
        textbox_submit = self.driver.find_element(By.ID,"submit")
        self.driver.execute_script('arguments[0].click()',textbox_submit)


    def download(self):
        upload_download = self.driver.find_element(By.ID,"item-7")
        self.driver.execute_script('arguments[0].click()',upload_download)
        upload_download_button = self.driver.find_element(By.ID,"downloadButton")
        self.driver.execute_script('arguments[0].click()',upload_download_button)


    def close(self):

        self.driver.quit()

if __name__ == '__main__':
    web_automation = WebAutomation()
    web_automation.login(username='azvikash',password='Python@123')
    web_automation.fill_form(name='Akash',email='Akash@gmail.com',cur_add='Kanuru',per_add='india')
    web_automation.close()
