import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given('I launch url on browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()


@given('I enter username and password')
def enterUserNameandPassword(context):
    time.sleep(5)
    context.driver.find_element_by_xpath(".//*[@id='txtUsername']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath(".//*[@id='txtUsername']").send_keys("Admin")
    time.sleep(2)
    context.driver.find_element_by_xpath(".//*[@id='txtPassword']").click()
    time.sleep(2)
    context.driver.find_element_by_xpath(".//*[@id='txtPassword']").send_keys("admin123")


@when('I click on login button')
def clickOnLoginButton(context):
    time.sleep(2)
    context.driver.find_element_by_id("btnLogin").click()


@then('I Should successfully login')
def validateLogin(context):
    context.driver.quit()
