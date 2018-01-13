# -*- coding: latin-1 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Driver():

    def __init__(self, element=None):
        self.driver = webdriver.Chrome()
        self.element = element

    def get_page(self, url):
        self.driver.get(url)

    def find_element(self, xpath):
        self.element = self.driver.find_element_by_xpath(xpath)
        return self.element

    def enter_text(self, text):
        self.element.send_keys(text)
        self.element.send_keys(Keys.ENTER)

    def click_button(self):
        self.element.click()

    def scroll_down(self, y):
        script = "window.scrollTo(0," + str(y) + ");"
        self.driver.execute_script(script)

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    # Test that driver loads the page
    from driver import Driver
    driver = Driver()
    driver.get_page('https://asunnot.oikotie.fi')

    # Test that driver finds the element
    time.sleep(1)
    xpath = '/html/body/footer/div[6]/div[1]/div/div/a[1]'
    driver.find_element(xpath)
    print(driver.element.text)

    # Test entering text to a search box
    time.sleep(1.5)
    xpath = '//input'
    driver.find_element(xpath)
    driver.enter_text('00510')

    # Test clicking a button
    time.sleep(2)
    driver.scroll_down(400)
    xpath = '/html/body/div[2]/section/div[4]/div[2]/button[2]'
    driver.find_element(xpath)
    driver.click_button()

    # End by scrolling down some more and then exit
    driver.scroll_down(300)
    time.sleep(5)
    # End test
    driver.quit()
