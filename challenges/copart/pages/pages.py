from selenium.webdriver.remote.webdriver import WebDriver


class Pages:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        yield
        self.driver.close()
