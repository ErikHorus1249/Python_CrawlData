
from TikiTarget import TikiTarget
from TikiItem import TikiItem
from TikiHelper import *
from bs4 import BeautifulSoup
import requests

TARGET_fILE = "target_list.txt"

targets = getTargetFromFile(TARGET_fILE)

# for target in targets:
#     print(target.info())


############################################################################################

target = targets[0]
searchLink = target.getSearchLink(2)
response =  requests.get(searchLink)


bsoup = BeautifulSoup(response.text,"lxml")
listElement = bsoup.find_all("a",{"class":"search-a-product-item"})
print(len(listElement))
i = 0
for e in listElement:
    # print(str(i) + ": " +"https://tiki.vn" + e.get("href"))
    if(e.get_text().find("Đã hết hàng") >= 0 or e.get_text().find("Ngừng kinh doanh") >= 0):
        print("có hết hàng")
        continue

    newItem = TikiItem()

    newItem.title = e.get("title")

    newItem.url = "https://tiki.vn" + e.get("href")

    span = e.find("span",{"class":"final-price"})
    newItem.price = convertToPrice(span.contents[0].strip())
    # print(str(price))
    span = e.find("span",{"class":"price-regular"})
    if(span != None):
        # print(convertToPrice(span.contents[0].strip()))
        newItem.regularPrice = convertToPrice(span.contents[0].strip())
    i += 1
    print(newItem.info())