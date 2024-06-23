from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class WebdriverInterface:

    LOGIN_URL = "https://vk.com/"
    URL = "https://vk.com/albums-71032788?z=photo-71032788_390836286%2Fphotos-71032788"

    def __init__(self):
        self.username = os.getenv('USERNAME', 'username not defined')
        self.password = os.getenv('PASSWORD', 'password not defined')
        try:
            self.driver = webdriver.Chrome(options=webdriver.ChromeOptions())
        except Exception as e:
            print(e)

    def auth(self):
        try:
            self.driver.get(url=self.LOGIN_URL)
        except Exception as e:
            print(e)
            return False
        return True

    def run_upload(self):
        first_page = input('input link of the first product: ')
        last_page_number = int(input('type the number of the last product: '))
        self.driver.get(url=first_page)
        img_url = self.driver.find_element(By.ID, 'pv_photo').find_element(By.TAG_NAME, 'img').get_attribute('src')
        print(img_url)
        time.sleep(40)

    def stop(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            print(e)
            return False
        return True
