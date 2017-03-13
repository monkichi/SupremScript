import urllib.request
import re
import webbrowser

htmlfile = urllib.request.urlopen("http://www.supremenewyork.com/shop")
htmltext = htmlfile.read().decode('utf-8')
htmlUrl = htmlfile.geturl()
htmlInfo = htmlfile.info()
htmlCode= htmlfile.getcode()
print (htmlUrl)
print(htmlInfo)
print(htmlCode)

#Get all the links html
mainPageLinks = re.findall('"((http|ftp)s?://.*?)"', htmltext)
#print(*mainPageLinks, sep='\n')

#Get Url for shopping all
allItemsPageUrl = mainPageLinks[2]
print(allItemsPageUrl[0])

#Open url for shop all
shopAllHtmlFile = urllib.request.urlopen(str(allItemsPageUrl[0]))
print (str(allItemsPageUrl[0]))
#Get html for shop all page
shopAllHtmlText = shopAllHtmlFile.read()
shopAllUrl = shopAllHtmlFile.geturl()
shopAllInfo = shopAllHtmlFile.info()
shopAllCode = shopAllHtmlFile.getcode()

#print(shopAllHtmlText)
print(shopAllUrl)
print(shopAllInfo)
print(shopAllCode)


#webbrowser.open(shopAllUrl, new=2)

urls = re.findall(r'href=[\'"]?([^\'" >]+)', str(shopAllHtmlText))
print(matches)

#Get all the links in the all page







                                
                                
