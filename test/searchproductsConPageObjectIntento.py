from utils.selenium_utils import SeleniumConnections

# create a new Firefox session
driver = SeleniumConnections.connect(10)

# navigate to the application home page
SeleniumConnections.open_web("https://magento.com/search/gss", driver)

# go to the search textbox
search_field = driver.find_element_by_id("edit-keys")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//@class['search-results']/../@class['gss-results']/../b")
# get the number of anchor elements found
print("Found " + str(len(products)) + " products:")
# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print (product.text)

#close the browser
driver.quit()