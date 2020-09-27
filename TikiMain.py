
from TikiTarget import TikiTarget
from TikiHelper import *
from bs4 import BeautifulSoup
import requests

TARGET_fILE = "target_list.txt"

targets = getTargetFromFile(TARGET_fILE)

# for target in targets:
#     print(target.info())


#########################

target = targets[0]
searchLink = target.getSearchLink(2)
response =  requests.get(searchLink)

# tim cac the
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
bsoup = BeautifulSoup(response.text,"lxml")
listElement = bsoup.find_all("a",{"class":"search-a-product-item"})
print(len(listElement))
i = 0
for e in listElement:
    # print(str(i) + ": " +"https://tiki.vn" + e.get("href"))
    span = e.find("span",{"class":"final-price"})
    price = convertToPrice(span.contents[0].strip())
    print(str(price))
    span = e.find("span",{"class":"price-regular"})
    if(span != None):
        print(convertToPrice(span.contents[0].strip()))
    i += 1