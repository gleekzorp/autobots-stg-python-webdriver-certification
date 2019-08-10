import unittest
from selenium import webdriver


class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get('https://www.copart.com/')
        popular_items_makes_models = self.driver.find_elements_by_xpath('//*[@id="tabTrending"]/div[1]//ul/li/a')

        for x in popular_items_makes_models:
            # print(x.get_attribute('innerHTML') + ' - ' + x.get_attribute('href'))
            print(f"{x.get_attribute('innerHTML')} - {x.get_attribute('href')}")


if __name__ == '__main__':
    unittest.main()
