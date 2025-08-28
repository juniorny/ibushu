import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random as ramdom

USER_NAME = os.environ.get("USER_NAME", '18718956189@163.com')
PASSWORD = os.environ.get("PASSWORD", 'key@1234')
MIN_STEP = int(os.environ.get("MIN_STEP", "20000"))
MAX_STEP = int(os.environ.get("MAX_STEP", "25000"))

FORM_URL = "https://gg.ibushu.com/"
TIMEOUT = 25
VERIFY_SELECTOR = '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a'
USER_INPUT_SELECTOR = '#zeppAccount'
PWD_INPUT_SELECTOR = '#zeppPassword'
STEP_INPUT_SELECTOR = '#step'
SUBMIT_SELECTOR = '#zepp > div > button'

STEP = str(ramdom.randint(MIN_STEP, MAX_STEP))

def main():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,2000")
    # 如遇不到位，可显式指定：/usr/bin/google-chrome
    # options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, TIMEOUT)

    try:
        driver.get(FORM_URL)

        # 等输入框出现并填写
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, VERIFY_SELECTOR)))
        button.click()
        time.sleep(2)

        # 等输入框出现并填写
        field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, USER_INPUT_SELECTOR)))
        field.clear()
        field.send_keys(USER)

        # 等输入框出现并填写
        field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, PWD_INPUT_SELECTOR)))
        field.clear()
        field.send_keys(PASSWORD)

        # 等输入框出现并填写
        field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, STEP_INPUT_SELECTOR)))
        field.clear()
        field.send_keys(STEP)

        time.sleep(1)

        # 滚动并点击提交
        btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SUBMIT_SELECTOR)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()

        # 截图留档
        driver.save_screenshot("after.png")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()