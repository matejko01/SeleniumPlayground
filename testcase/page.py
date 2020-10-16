from locator import MainPageLocators
from locator import PyconSearchLocators
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"

class BasePage():
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def title_check(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_about_button(self):
        element = self.driver.find_element(*MainPageLocators.ABOUT_BUTTON)
        element.click()


class PyconSearchPage(BasePage):
    def is_page_found(self):
        return "Page not found" not in self.driver.page_source

    def click_conferences_and_workshops_button(self):
        element = self.driver.find_element(*PyconSearchLocators.CONFERENCES_AND_WORKSHOPS_BUTTON)
        element.click()