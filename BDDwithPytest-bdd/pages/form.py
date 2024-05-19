from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os.path


class FormPage:
    LOCATION = "https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a"
    CONTINUE_BUTTON = (By.XPATH, '//span[text()="CONTINUE"]')
    START_BUTTON = (By.XPATH, '//span[text()="START"]')
    KEVIN_BUTTON = (By.XPATH, '//span[text()="Making a case against Kevin"]')
    BLAME_BUTTON = (By.XPATH, '//span[text()="Who is to blame?"]')
    JUDGE_THIS_BUTTON = (By.XPATH, '//span[text()="JUDGE THIS"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.LOCATION)

    def continue_button_click(self):
        continue_btn = self.browser.find_element(*self.CONTINUE_BUTTON)
        continue_btn.click()

    def start_button_click(self):
        start_btn = self.browser.find_element(*self.START_BUTTON)
        start_btn.click()

    def select_kevin_case(self):
        kevin_btn = self.browser.find_element(*self.KEVIN_BUTTON)
        kevin_btn.click()
    def select_who_to_blame(self):
        kevin_btn = self.browser.find_element(*self.BLAME_BUTTON)
        kevin_btn.click()

    def select_judge_this(self):
        judge_btn = self.browser.find_element(*self.JUDGE_THIS_BUTTON)
        judge_btn.click()
