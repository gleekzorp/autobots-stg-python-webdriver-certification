from selenium import webdriver


def test_01_challenge():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    assert 'Google' in driver.title
