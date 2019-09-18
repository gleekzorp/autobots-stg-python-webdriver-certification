from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_06_challenge():
    driver = webdriver.Chrome()
    driver.get('https://www.copart.com')
    search_make = 'nissan'
    search_model = 'skyline'
    driver.find_element(By.ID, "input-search").send_keys(search_make + Keys.ENTER)

    drop_down = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='#collapseinside4']"))
    )
    drop_down.click()

    driver.find_element(By.XPATH, "//*[@id='collapseinside4']//form//input").send_keys(search_model)
    try:
        driver.find_element(By.XPATH, f"//input[@value='{search_model}']")
    except:
        driver.save_screenshot(f'{search_make}_{search_model}_not_found.png')
    else:
        print('You found it!')
    driver.close()