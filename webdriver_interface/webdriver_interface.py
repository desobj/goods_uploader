from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os


class WebdriverInterface:

    URL = "https://srlt.msi.com/"

    def __init__(self):
        try:
            self.driver = webdriver.Chrome(service=Service(executable_path=os.getenv('WD_PATH', 'wd_path not defined')))
        except Exception as e:
            print(e)

    def auth(self):
        try:
            username = os.getenv('USERNAME', 'username not defined')
            password = os.getenv('PASSWORD', 'password not defined')
            self.driver.get(url=self.URL)
            time.sleep(5)
            login_input = self.driver.find_element(By.ID, 'username')
            login_input.clear()
            login_input.send_keys(username)
            login_input = self.driver.find_element(By.ID, 'password')
            login_input.clear()
            login_input.send_keys(password)
            time.sleep(3)
            self.driver.find_element(By.ID, 'submit').click()  # submit_button
        except Exception as e:
            print(e)
            return False
        return True

    def run_upload(self):
        while True:
            for rma_number in input('Type RMA Numbers: ').split(','):
                self.make_tcc_confirm(rma_number)

    def make_tcc_confirm(self, rma_number):
        try:
            self.driver.get('https://srlt.msi.com/iFramePage/ASP_First_Page')  # asp_repair_v3_button
            time.sleep(3)
            self.driver.find_element(By.ID, 's2id_rcSiteName').click()  # pop-up_window
            time.sleep(3)
            # asp_choose
            self.driver.find_elements(By.CLASS_NAME, 'select2-result-label')[self.get_service_type(rma_number)].click()

            time.sleep(8)
            self.driver.find_element(By.ID, 'rmano').click()
            self.driver.find_element(By.ID, 'rmano').send_keys(rma_number)  # rma_number_fill_field
            time.sleep(3)
            self.driver.find_element(By.ID, 'btnContinue').click()  # next_button
            time.sleep(10)
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "IFRAME1"))
            time.sleep(3)
            self.driver.find_element(By.ID, 'txtErrorC')  # error_code
            self.driver.find_element(By.ID, 'txtErrorC').send_keys("NXSEV")
            self.driver.find_element(By.ID, 'txtRMAC')
            self.driver.find_element(By.ID, 'txtRMAC').send_keys("NXN00")
            self.driver.find_element(By.ID, 'txtRRemark')
            self.driver.find_element(By.ID, 'txtRRemark').send_keys("TCC CONFIRMED")
            time.sleep(3)
            self.driver.find_element(By.ID, 'Button4').click()
            time.sleep(10)
            self.driver.find_element(By.ID, 'Button5').click()
            time.sleep(3)
            self.driver.switch_to.alert.accept()
        except Exception as e:
            print(e)
            return False
        time.sleep(10)
        return True

    def stop(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            print(e)
            return False
        return True
