from selenium import webdriver
import unittest
import page
import time

class PythonOrgTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"D:\pliki\chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_one(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        pycon_page = page.PyconSearchPage(self.driver)
        pycon_page.click_conferences_and_workshops_button()
        assert pycon_page.is_page_found()
        time.sleep(5)
        self.driver.back()
        time.sleep(5)
        main_page.search_text_element = "tutorial"
        main_page.click_go_button()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()