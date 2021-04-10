import requests, re
from bs4 import BeautifulSoup

"""
We want to loop through all the men clothing pages
untill there is no clothes left.

?? maybe there are a total of 89 pages worth of clothing

for each cloth we want to get its:
  - designer name
  - cloth title
  - price
  - image    
"""

# maybe append to an excel spread sheet?
items = []
isRun = True
i = 1

def findChildElem(rootElem, parentTag, childTag):
    return rootElem.find(parentTag).find(childTag, {'title': re.compile('.*')}, recursive=False)
         

while isRun:
    html = requests.get(f"https://www.factory54.co.il/men/clothing?p={i}").text
    soup = BeautifulSoup(html, 'html.parser')
    clothes = soup.findAll('div', {'class':'woman_item clearfix'})

    for cloth in clothes:
        img = cloth.find('img', {'class': ['lazy-img', 'default', 'processed']})
        designer = findChildElem(cloth, 'h2', 'a')
        clothTitle = findChildElem(cloth, 'p', 'a')
        price = cloth.find('span', {'class':'price'})
        # We do not need to check all of the properties
        if designer is None:
           isRun = False
           i = 0
           break
        print(f"Designer: {designer['title']}, {clothTitle['title']}, price:{price.string}")
        items.append(f"Designer: {designer['title']}, {clothTitle['title']}, price:{price.string}")
    i += 1    
