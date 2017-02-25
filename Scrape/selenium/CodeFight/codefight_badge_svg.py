from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse


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
driver.set_window_size(710, 602)
driver.get("https://codefights.com/leaderboard")
img_src = set()
# inputElement = driver.find_element_by_id("lst-ib")
# inputElement.send_keys("Cheese!")
# submit the form (although google automatically searches now without
# submitting)
# inputElement.submit()

# the page is ajaxy so the title is originally this:
file = open("badge_src.txt", "w")
try:
    # we have to wait for the page to refresh, the last thing that seems to be
    # updated is the title
    # WebDriverWait(driver, 100).until(EC.title_contains("Cheese!"))
    while (True):
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table--cell-rank"))
        )
        elements = driver.find_elements(
            By.CSS_SELECTOR, ".leaderboard .table--body-row")
        for element in elements:
            src = element.find_element(
                By.CSS_SELECTOR, ".table--cell-level img").get_attribute("src")
            print(src)
            img_src.add(src)
        next_btn = driver.find_element(
            By.CSS_SELECTOR, ".pagination .button:last-child")
        next_btn.click()
        # break
finally:
    for item in img_src:
        file.write("%s\n" % item)
    print("Quitting")
    file.close()
    driver.quit()
