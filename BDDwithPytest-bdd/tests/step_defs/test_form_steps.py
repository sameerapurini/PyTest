from pages.form import FormPage
from pytest_bdd import scenarios, given, when, then
import time


scenarios('../features/form.feature')

def form(browser):
    form = FormPage(browser)
    return form

@given('I go to the Main page to select a case')
def gotoMainPage(browser):
    form = FormPage(browser)
    form.load()
    time.sleep(1)
    return form

@given('I click the START button')
def start_button_click(browser):
    form(browser).start_button_click()
    time.sleep(2)

@when('I select case of Kevin')
def select_kevin_case(browser):
    form(browser).select_kevin_case()

@when('I select who is to blame')
def select_whom_to_blame(browser):
    form(browser).select_who_to_blame();


@then('I judge the selected case')
def judge_kevin_startr(browser):
    form(browser).select_judge_this()
