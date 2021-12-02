from selenium import webdriver

class Record:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://recordtv.r7.com/power-couple-brasil-5'

    def navigate(self):
        self.driver.get(self.url)

ff = webdriver.Firefox()
g = Record(ff)


#voting-button--hidden
