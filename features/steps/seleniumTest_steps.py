from behave import *
from utils.selenium_utils import SeleniumConnections


@given('I am on home page')
def step_i_am_on_home_page(context):
    # context.driver.get("https://magento.com/search/gss")
    SeleniumConnections.open_web("https://magento.com/search/gss", context.driver)


@when('I search for {text}')
def step_i_search_for(context, text):
    search_field = context.driver.find_element_by_id("edit-keys")
    search_field.clear()
    search_field.send_keys("phones")
    search_field.submit()


@then('I should see list of matching products in search results')
def step_i_should_see_list(context):
    products = context.driver.find_elements_by_xpath("//@class['search-results']/../@class['gss-results']/../b")
    assert len(products) > 0