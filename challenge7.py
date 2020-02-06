import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common2.navigateTo import navigateTo


class challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        elements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        theDict = dict()

        for model in elements:
            try:
                ng = navigateTo()
                theText = model.text
                theDict[theText] = model.get_attribute("href")
                print(theText + " - " + theDict[theText])

                if ng.goTo(theDict[theText], theText):
                    print("Successfully navigated to the " + theText + " page")
                else:
                    print("Failed to navigate to the " + theText + " page")

            except:
                print("There was error")


if __name__ == '__main__':
    unittest.main()