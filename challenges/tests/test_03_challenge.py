from selenium import webdriver
from selenium.webdriver.common.by import By


def test_03_challenge_a():
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    popular_makes_models = driver.find_elements(By.XPATH, '//*[@id="tabTrending"]/div[1]//ul/li/a')
    print_results(popular_makes_models)
    assert len(popular_makes_models) == 20


def test_03_challenge_b():
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    popular_categories = driver.find_elements(By.XPATH, '//*[@ng-if="popularSearches"]/../div[3]//a')
    print_results(popular_categories)
    assert len(popular_categories) == 20


def print_results(items):
    print("\n")
    for item in items:
        print(f"{item.text} - {item.get_attribute('href')}")
