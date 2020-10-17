from selenium.webdriver.common.by import By

class MainPageLocators():
    GO_BUTTON = (By.ID, "submit")
    ABOUT_BUTTON = (By.ID, "about")

class PyconSearchLocators():
    CONFERENCES_AND_WORKSHOPS_BUTTON = (By.XPATH, "//*[@id=\"content\"]/div/section/form/ul/li[2]/h3/a")
