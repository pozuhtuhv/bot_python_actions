from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저 창을 열지 않고 실행
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 크롬드라이버 경로 설정
chrome_driver_path = '/usr/bin/chromedriver'
service = Service(chrome_driver_path)

# 드라이버 시작
driver = webdriver.Chrome(service=service, options=options)

# 페이지 열기
driver.get("https://www.instiz.net")

print(driver.page_source)

driver.quit()
