import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_younique_cart():
    driver = webdriver.Chrome()
    driver.get('https://www.youniqueproducts.com/products/view/US-51081-01#.XZaQI-dKjyU')
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "[class*='addToCartBtn']")
    add_to_cart_button.click()
    checkout_button = driver.find_element(By.CSS_SELECTOR, "[class*='icon-cart']")
    checkout_button.click()

    time.sleep(2)

    checkout_overview_array = driver.find_elements(By.XPATH, "//*[@id='cartview']//td[contains(@class,'total')]")

    time.sleep(2)

    dict = {}

    for i in range(2, len(checkout_overview_array)-2, 2):
        dict[checkout_overview_array[i].text] = checkout_overview_array[i + 1].text
    print(dict)

    for i in range(2, len(checkout_overview_array)-2, 2):
        print(f"i = #{i}: {checkout_overview_array[i].text}")
        if checkout_overview_array[i].text == "Total Items:":
            assert checkout_overview_array[i + 1].text == "1"
        if checkout_overview_array[i].text == "Subtotal:":
            assert checkout_overview_array[i + 1].text == "$12.00"
        if checkout_overview_array[i].text == "Shipping:":
            assert checkout_overview_array[i + 1].text == "$5.50"
        if checkout_overview_array[i].text == "Total Balance Due:":
            assert checkout_overview_array[i + 1].text == "$17.50 USD"

    # counter = 0
    # for item in checkout_overview_array:
    #     print(f"counter#{counter}: {item.text}")
    #     counter += 1
    #     if item.text == "Total Items:":
    #         assert checkout_overview_array[counter].text == "1"
    #     if item.text == "Subtotal:":
    #         assert checkout_overview_array[counter].text == "$12.00"
    #     if item.text == "Shipping:":
    #         assert checkout_overview_array[counter].text == "$5.50"
    #     if item.text == "Total Balance Due:":
    #         assert checkout_overview_array[counter].text == "$17.50 USD"




###### Extra stuff for reference until I solve this #####
    # counter = 0
    # while counter < len(checkout_overview_array):
    #     print(checkout_overview_array[counter].text)
    #     counter += 1

    # //*[@id="cartview"]//tbody//tr/td
    # print(checkout_overview_array)
    # for item in checkout_overview_array:
    #     print(item.text)

# //*[@id='cartview']//tbody//tr/td
# totalLbls
# //*[@id='cartview']//td[contains(@class,'total')]
# checkout_overview_array = driver.find_elements(By.CSS_SELECTOR, "[class*='totalDisplay")
# checkout_overview_array = driver.find_elements(By.XPATH, "//*[@id='cartview']//tbody//tr/td")
# checkout_overview_array = driver.find_elements(By.XPATH, "//*[@id='cartview']//tbody//*[contains(@class,'total')]")
