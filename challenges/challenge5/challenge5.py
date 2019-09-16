import collections
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        search_term = 'porsche'
        self.driver.get("https://www.copart.com")
        self.driver.find_element_by_id('input-search').send_keys(search_term)
        self.driver.find_element_by_class_name('search-icon').click()
        show_how_many_entries_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="serverSideDataTable_length"]//select'))
        )
        show_how_many_entries_button.click()
        option_one_hundred = self.driver.find_element_by_xpath("//*[@id='serverSideDataTable_length']//option[3]")
        option_one_hundred.click()

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "serverSideDataTable_processing"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.ID, "serverSideDataTable_processing"))
        )

        model_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@data-uname="lotsearchLotmodel"]'))
        )
        damage_type_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@data-uname="lotsearchLotdamagedescription"]'))
        )


        # Model Attempt 1
        # models = []
        # for model in model_list:
        #     if model.get_attribute('innerHTML') == '[[ lm ]]':
        #         continue
        #     else:
        #         models.append(model.get_attribute('innerHTML'))

        # models_dictionary = collections.Counter(models)
        # for keys in models_dictionary:
        #     print(keys, '-', models_dictionary[keys])


        # Model Attempt 2
        # models_dictionary = {}
        #
        # for model in model_list:
        #     model_inner_html = model.get_attribute('innerHTML')
        #     if model_inner_html == '[[ lm ]]':
        #         continue
        #     if model_inner_html in models_dictionary:
        #         models_dictionary[model_inner_html] += 1
        #     else:
        #         models_dictionary[model_inner_html] = 1
        #
        # print(models_dictionary)


        # Model Attempt 3
        models_dictionary = collections.Counter()
        for model in model_list:
            models_dictionary[model.get_attribute('innerHTML')] += 1
        print(models_dictionary)

        # Damage Types
        damage_types = {
            'REAR END': 0,
            'FRONT END': 0,
            'MINOR DENT/SCRATCHES': 0,
            'UNDERCARRIAGE': 0,
            'MISC': 0
        }
        for damage_type in damage_type_list:
            if damage_type.get_attribute('innerHTML') == 'REAR END':
                damage_types['REAR END'] += 1
            elif damage_type.get_attribute('innerHTML') == 'FRONT END':
                damage_types['FRONT END'] += 1
            elif damage_type.get_attribute('innerHTML') == 'MINOR DENT/SCRATCHES':
                damage_types['MINOR DENT/SCRATCHES'] += 1
            elif damage_type.get_attribute('innerHTML') == 'UNDERCARRIAGE':
                damage_types['UNDERCARRIAGE'] += 1
            else:
                damage_types['MISC'] += 1
        print(damage_types)


if __name__ == '__main__':
    unittest.main()
