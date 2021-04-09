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

items = []

def findChildElem(rootElem, parentTag, childTag):
    return rootElem.find(parentTag).find(childTag, {'title': re.compile('.*')}, recursive=False)
         


for i in range(1, 10):
    html = requests.get(f"https://www.factory54.co.il/men/clothing?p={i}").text
    soup = BeautifulSoup(html, 'html.parser')
    clothes = soup.findAll('div', {'class':'woman_item clearfix'})

    for cloth in clothes:
        img = cloth.find('img', {'class': ['lazy-img', 'default', 'processed']})
        designer = findChildElem(cloth, 'h2', 'a')
        clothTitle = findChildElem(cloth, 'p', 'a')
        price = cloth.find('span', {'class':'price'})
        # print(price.string)
        #print(clothTitle['title'])
        # print(designer['title'])
        # print(img['data-src'])
        items.append(f"Designer: {designer['title']}, {clothTitle['title']}, price:{price.string}")

print(len(items))        
