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
# items = []
isRun = True
i = 1

def findChildElemByTitle(rootElem, parentTag, childTag):
    return rootElem.find(parentTag).find(childTag, {'title': re.compile('.*')}, recursive=False)

# classDef can be a list of str's or str
def findElemByClass(rootElem, tag, classDef):
    return cloth.find(tag, {'class': classDef})
         

while isRun:
    html = requests.get(f"https://www.factory54.co.il/men/clothing?p={i}").text
    soup = BeautifulSoup(html, 'html.parser')
    clothes = soup.findAll('div', {'class':'woman_item clearfix'})

    for cloth in clothes:
        img = findElemByClass(cloth, 'img', ['lazy-img', 'default', 'processed'])
        designer = findChildElemByTitle(cloth, 'h2', 'a')
        clothTitle = findChildElemByTitle(cloth, 'p', 'a')
        price = findElemByClass(cloth, 'span', 'price')
        if designer is None:
           isRun = False
           i = 0
           break
        print(f"Designer: {designer['title']}\n{clothTitle['title']}\nprice:{price.string}\n{img['data-src']}")
        print("------------------------------------------------------------")
        # items.append(f"Designer: {designer['title']}, {clothTitle['title']}, price:{price.string}")
    i += 1    
