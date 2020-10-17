from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

path = r"D:\pliki\chromedriver.exe"

first_name = "Luke"
last_name = "Smith"
email_address = f"{first_name}.{last_name}@mail.com"
password = f"{first_name}'s password"
address = "Elm Street 12/12"
city = "Springwood"
postal_code = "46077"
mobile_phone = "666 444 8887"
address_alias = "My Address"

driver = webdriver.Chrome(path)

driver.get("http://automationpractice.com/index.php")

def find_element_by(element_type, locator):
    if element_type == "class_name":
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_class_name(locator))
        element = driver.find_element_by_class_name(locator)
        return element
    elif element_type == "id":
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id(locator))
        element = driver.find_element_by_id(locator)
        return element

def click_sign_up():
    sign_up_button = find_element_by("class_name", "login")
    sign_up_button.click()

def provide_email():
    email_textbox = find_element_by("id", "email_create")
    email_textbox.send_keys(email_address)

    submit_button = find_element_by("id", "SubmitCreate")
    submit_button.click()

def provide_personal_info():
    title_checkbox = find_element_by("id", "id_gender1")
    title_checkbox.click()

    first_name_textbox = find_element_by("id", "customer_firstname")
    first_name_textbox.send_keys(first_name)

    last_name_textbox = find_element_by("id", "customer_lastname")
    last_name_textbox.send_keys(last_name)

    password_textbox = find_element_by("id", "passwd")
    password_textbox.send_keys(password)

    birth_days = Select(find_element_by("id", "days"))
    birth_days.select_by_value("15")

    birth_months = Select(find_element_by("id", "months"))
    birth_months.select_by_value("12")

    birth_years = Select(find_element_by("id", "years"))
    birth_years.select_by_value("1984")

def provide_address():
    address_texbox = find_element_by("id", "address1")
    address_texbox.send_keys(address)

    city_textbox = find_element_by("id", "city")
    city_textbox.send_keys(city)

    state_selection = Select(find_element_by("id", "id_state"))
    state_selection.select_by_value("14")

    postal_code_textbox = find_element_by("id", "postcode")
    postal_code_textbox.send_keys(postal_code)

    country_selection = Select(find_element_by("id", "id_country"))
    country_selection.select_by_value("21")

    phone_number_textbox = find_element_by("id", "phone_mobile")
    phone_number_textbox.send_keys(mobile_phone)

    address_alias_textbox = find_element_by("id", "alias")
    address_alias_textbox.send_keys(address_alias)

    submit_account_button = find_element_by("id", "submitAccount")
    submit_account_button.click()

def verify_creation():
    if driver.title == "My account - My Store":
        print("registration successful")
    else:
        print("registration failed")










click_sign_up()
provide_email()
provide_personal_info()
provide_address()
verify_creation()