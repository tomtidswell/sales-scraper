import csv
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


dbclient = MongoClient('mongodb://localhost/')
sales_data = dbclient["sales"]
collection = sales_data["products"]
collection.drop()
# mydict = {
#     "name": "Pure Cotton Luxury Spa Towel",
#     "prices": ['Sale price', '£6.00 - £18.00', 'Previous price'],
#     "url": "https://www.marksandspencer.com/pure-cotton-luxury-spa-towel/p/hbp60467039?color=WHITE#intid=prodColourId-60467042",
#     "badge": "40% off"
# }
# x = collection.insert_one(mydict)



feedname = "marksandspencer-home"
site = "https://www.marksandspencer.com"
page = "/l/offers/home-offers"


page = requests.get(f"{site}{page}")
soup = BeautifulSoup(page.text, 'html.parser')
# product_grid = soup.find_all('ul', class_='grid')
# print(product_grid)
grid_items = soup.find_all('li', class_='grid__tile')
products = []

for p in grid_items:
    p_data = {}
    p_data['name'] = p.find(class_='product__title').text
    p_data['prices'] = []
    for child in p.find(class_='sale-price').descendants:
        if isinstance(child, type('bs4.element.NavigableString')):
            p_data['prices'].append(child.string)
    p_data['url'] = f"{site}{p.a['href']}"
    p_data['badge'] = p.find(class_='product__badge').text
    products.append(p_data)
    collection.insert_one(p_data)


# with open(f'data/{feedname}.csv', 'w') as f:
#     w = csv.DictWriter(f, products[0].keys())
#     w.writeheader()
#     for row in products:
#         w.writerow(row)
