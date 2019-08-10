import unittest
from selenium import webdriver


class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def test_challenge2(self):
        self.driver.get("https://www.amazon.com")
        self.assertIn("Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more", self.driver.title)

    def test_challenge3(self):
        self.driver.get("https://www.yahoo.com")
        self.assertIn("Yahoo", self.driver.title)

    def test_challenge4(self):
        self.driver.get("https://www.msn.com")
        self.assertIn("MSN | Outlook, Office, Skype, Bing, Breaking News, and Latest Videos", self.driver.title)


if __name__ == '__main__':
    unittest.main()


