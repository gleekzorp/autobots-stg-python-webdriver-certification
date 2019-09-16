from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_challenge():
    driver = webdriver.Chrome()
    driver.get('https://www.copart.com')
    search_term = 'exotics'
    search_word = 'MASERATI'

    driver.find_element(By.ID, "input-search").send_keys(search_term + Keys.ENTER)
    results_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "serverSideDataTable")))
    assert search_word in results_page.text
