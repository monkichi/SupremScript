from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

# create a new Firefox session

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
 
# navigate to the application home page

driver.get("http://www.supremenewyork.com/shop/new")
newItemsPageSource = driver.page_source
#newItemLinks = re.findall(r'(?<=<a href=")[^"]*', newItemsPageSource)
newItemLinks = re.findall(r'href=[\'"]?([^\'" >]+)', newItemsPageSource)
print(len(newItemLinks))
#print(newItemsPageSource)
print '[%s]' % ', '.join(map(str, newItemLinks))

matching = [s for s in newItemLinks if "/shop/jackets/" in s]
print '[%s]' % ', '.join(map(str, matching))
url = "".join(["http://www.supremenewyork.com/", matching[0]])
driver.get(url)

#get data from item page
selectedItemPageSource = driver.page_source
print(selectedItemPageSource)


driver.get("http://www.supremenewyork.com/shop/shirts/lia9ben4m/vugbr87sh")
selectedItemPageSource = driver.page_source
print(selectedItemPageSource)

#chose size
sizeId =



#driver.findElement(By.xpath("//a[@href='/shop/shirts/lia9ben4m/dt1287u9f']")).click()

#def clickLinkByHref(href) :
#    List<WebElement> anchors = driver.findElements(By.tagName("a")
#    Iterator<WebElement> i = anchors.iterator()
#    
#    while(i.hasNext())
#        WebElement anchor = i.next()
#            #if(anchor.getAttribute("href").contains(href)) {
#            #anchor.click();
#            #break;

        


