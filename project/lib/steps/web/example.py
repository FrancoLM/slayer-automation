import logging
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

from project.lib.steps.common.decorators import log_exec_time


@step("I open a browser")
def step_impl(context, maximized=True):
    logging.debug("Testing printing")
    logging.error("Error message")
    context.driver = webdriver.Chrome()
    if maximized:
        context.driver.maximize_window()


@step("I go to the Google web page")
@log_exec_time
def step_impl(context):
    context.driver.get("https://www.google.com")
    context.driver.get_screenshot_as_file(os.path.join(os.getcwd(), "output", "Google_page.png"))
    time.sleep(3)


@step("I wait for an invalid element")
def step_impl(context):
    context.driver.find_element(By.ID, "invalid")
    time.sleep(3)