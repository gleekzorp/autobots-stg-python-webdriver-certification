import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# import time


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        search_term = "exotics"
        search_word = 'ROLLS-ROYCE'
        self.driver.get('https://www.copart.com/')
        # input_field = self.driver.find_element_by_id('input-search')
        # input_field.send_keys(search_term)
        # input_field.send_keys(Keys.ENTER)

        # How to chain
        self.driver.find_element_by_id('input-search').send_keys(search_term + Keys.ENTER)

        results_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "serverSideDataTable"))
        )
        # Another way to wait
        # time.sleep(5)
        # results_table = self.driver.find_element_by_id('serverSideDataTable')

        results_table_source = results_table.get_attribute('innerHTML')
        self.assertIn(search_word, results_table_source)

        # print(results_table_source)


if __name__ == '__main__':
    unittest.main()