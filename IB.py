from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class InstagramBot:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(1)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(1)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)



    def like_photo(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(1)
        pic_hrefs = []

        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                          if '.com/p/' in elem.get_attribute('href')]
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            #except Exception as e:
             #   continue

        unique_photos = len(pic_hrefs)

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-lable="LIke"]').click()
                like_button().click()
            except Exception as e:
                time.sleep(2)

        unique_photos -= 1


if __name__ == "__main__":
    username = "sapra5298"
    password = "anishashish13"
    ig = InstagramBot(username, password)
    ig.login()

    hashtag = 'amazing'
    ig.like_photo(hashtag)
