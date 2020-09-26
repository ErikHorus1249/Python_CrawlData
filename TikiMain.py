
from TikiTarget import TikiTarget
from TikiHelper import *
import requests

TARGET_fILE = "target_list.txt"

targets = getTargetFromFile(TARGET_fILE)

# for target in targets:
#     print(target.info())


#########################

target = targets[0]
searchLink = target.getSearchLink(2)
response =  requests.get(searchLink)
# print(searchLink)
print(response.text)
