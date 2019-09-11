import unittest
from selenium import webdriver


class Challenge3(unittest.TestCase):

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

        counter = 0
        while counter < len(popular_items_makes_models):
            print(popular_items_makes_models[counter].get_attribute('innerHTML') + ' - ' + popular_items_makes_models[counter].get_attribute('href'))
            counter += 1

    def test_challenge3_categories(self):
        self.driver.get('https://www.copart.com/')
        categories = self.driver.find_elements_by_xpath('//*[@ng-if="popularSearches"]/../div[3]//a')

        for x in categories:
            # print(x.get_attribute('innerHTML') + ' - ' + x.get_attribute('href'))
            print(f"{x.get_attribute('innerHTML')} - {x.get_attribute('href')}")

        counter = 0
        while counter < len(categories):
            print(categories[counter].get_attribute('innerHTML') + ' - ' + categories[counter].get_attribute('href'))
            counter += 1


if __name__ == '__main__':
    unittest.main()
