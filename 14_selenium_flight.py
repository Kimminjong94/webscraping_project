from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

#d이번달 27일 ,28일 선택
# browser.find_elements_by_link_text("27")[0].click()
# browser.find_elements_by_link_text("28")[0].click()

# browser.find_elements_by_link_text("27")[1].click() #다음달
# browser.find_elements_by_link_text("28")[1].click()

#d이번달 27일 다음달 28일
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()

#항공권 검색
browser.find_element_by_link_text("항공권 검색").click()


try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]/div[4]/div/div/div[1]/span[1]")))
    print(elem.text)

finally:
    browser.quit()

# #첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]/div[4]/div/div/div[1]/span[1]")
# print(elem.text)