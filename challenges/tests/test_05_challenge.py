import collections

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_05_challenge():
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    search_term = "porsche"
    driver.find_element(By.ID, 'input-search').send_keys(search_term + Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="serverSideDataTable"]')))
    Select(driver.find_element(By.XPATH, '//*[@id="serverSideDataTable_length"]//select')).select_by_value('100')

    # Spinner
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "serverSideDataTable_processing"))
    )
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.ID, "serverSideDataTable_processing"))
    )

    # Models
    model_list = driver.find_elements(By.XPATH, '//*[@data-uname="lotsearchLotmodel"]')
    models_dictionary = collections.Counter()
    for model in model_list:
        models_dictionary[model.get_attribute('innerHTML')] += 1
    print_models_results(models_dictionary)

    # Damage Types
    damage_type_list = driver.find_elements(By.XPATH, '//*[@data-uname="lotsearchLotdamagedescription"]')
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
    print_damage_type_results(damage_types)


def print_models_results(models):
    print('\n MODELS: \n')
    for model_key, model_value in models.items():
        if model_key == "[[ lm ]]":
            pass
        else:
            print(f"{model_key}: {model_value}")


def print_damage_type_results(damage_types):
    print('\n DAMAGE-TYPES: \n')
    for damage_type_key, damage_type_value in damage_types.items():
        print(f"{damage_type_key}: {damage_type_value}")
