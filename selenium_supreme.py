from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support.ui import Select

# create a new Firefox session

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
 
# navigate to the application home page
driver.get("http://www.supremenewyork.com/shop/new")
#get source code of new items
newItemsPageSource = driver.page_source
#get all the links in new items
newItemLinks = re.findall(r'href=[\'"]?([^\'" >]+)', newItemsPageSource)
print(len(newItemLinks))
#print(newItemsPageSource)
print '[%s]' % ', '.join(map(str, newItemLinks))
#find links with /shop/jackets
matching = [s for s in newItemLinks if "/shop/jackets/" in s]
print '[%s]' % ', '.join(map(str, matching))
url = "".join(["http://www.supremenewyork.com/", matching[0]])
driver.get(url)

#get data from item page
selectedItemPageSource = driver.page_source
print(selectedItemPageSource)


driver.get("http://www.supremenewyork.com/shop/shirts/lt3u51bym/m1x5yralp")
selectedItemPageSource = driver.page_source
#print(selectedItemPageSource)
#

##chose size
select = Select(driver.find_element_by_id('size'))

for i , option in enumerate(select.options):
    print(i, option.text)
    if option.text=='XLarge':
        option.click()
    else:
        print("No X-Large availabe")

#add item to cart after choosing size
driver.find_element_by_xpath("//input[@type='submit' and @value='add to cart']").click()

#find keep shopping button
#driver.find_element_by_class_name("buttoncontinue").click()


#.....
log_but3 = "//a[@class='button continue']"
driver.find_element_by_xpath(log_but3).click()

driver.implicitly_wait(1)
log_but2 = "//a[@class='button checkout']"
driver.find_element_by_xpath(log_but2).click()


#get page source of checkout
checkOutPageSource = driver.page_source

order_billing_name = driver.find_element_by_id('order_billing_name')
billingNameString = "Christian Zamudio"
order_billing_name.send_keys(billingNameString)

order_email = driver.find_element_by_id('order_email')
billingEmailString = "zamuchristian@gmail.com"
order_email.send_keys(billingEmailString)
        
order_phone = driver.find_element_by_id('order_tel')
billingPhoneString = "8187921821"
order_phone.send_keys(billingPhoneString)

order_address = driver.find_element_by_id('bo')
billingAddressString = "8530 cedros ave apt 4 "
order_phone.send_keys(billingAddressString)

order_zip = driver.find_element_by_id('order_billing_zip')
billingPhoneString = "91402"
order_phone.send_keys(billingPhoneString)

order_billing_city = driver.find_element_by_id('order_billing_city')
billingCityString = "Panorama City"
order_phone.send_keys(billingCityString)

#select state
selectBillingState = Select(driver.find_element_by_id('order_billing_state'))

for i , option in enumerate(selectBillingState.options):
    print(i, option.text)
    if option.text=='CA':
        option.click()

#select state
selectCardType = Select(driver.find_element_by_id('credit_card_type'))

for i , option in enumerate(selectCardType.options):
    print(i, option.text)
    if option.text=='Visa':
        option.click()

order_card_number = driver.find_element_by_id('cnb')
billingCardNumberString = "00000000000000"
order_card_number.send_keys(order_card_number)

selectCardMonth = Select(driver.find_element_by_id('credit_card_month'))

for i , option in enumerate(selectCardMonth.options):
    print(i, option.text)
    if option.text=='01':
        option.click()

selectCardYear = Select(driver.find_element_by_id('credit_card_year'))

for i , option in enumerate(selectCardYear.options):
    print(i, option.text)
    if option.text=='2020':
        option.click()

checkOrderTerm = driver.find_element_by_id("order_terms").click()



