from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import json


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--driver", type=str, default="chrome",
                help="which driver to use")

args = vars(ap.parse_args())
choice = args["driver"]
driver = ""
if(choice == "firefox"):
    driver = webdriver.Firefox()
else:
    driver = webdriver.Chrome()
driver.set_window_size(718, 726)
driver.get("https://m.facebook.com/")
with open('credentials.json') as data_file:
    data = json.load(data_file)
    emailElement = driver.find_element_by_name("email")
    emailElement.send_keys(data["email"])
    passElement = driver.find_element_by_name("pass")
    passElement.send_keys(data["password"])
    driver.find_element_by_name("login").click()
    try:
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "._2pii a"))
        )
        driver.find_element(
            By.CSS_SELECTOR, "._2pii a").click()
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "._4g34 textarea"))
        )
        status = raw_input("What's On Your Mind?\n")
        # status = "Updating Status From #Selenium is Cool !"
        statusElement = driver.find_element(By.CSS_SELECTOR, "._4g34 textarea")
        statusElement.send_keys(status)
        driver.find_element(By.CSS_SELECTOR, "._5s61 button").click()
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '._58jw p'), status))
        )
    finally:
        print("Quitting")
        driver.quit()
