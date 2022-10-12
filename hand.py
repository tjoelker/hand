import requests
from bs4 import BeautifulSoup
from csv import writer
from lxml import etree

# get product catalog and append into array
catalog = []
def get_product_catalog() :
  request = requests.get('https://www.ah.nl/sitemaps/entities/products/detail.xml')
  soup = BeautifulSoup(request.text, 'xml')
  product_catalog = soup.find_all('loc')
  for product in product_catalog :
    catalog.append(product.get_text())

  return catalog

get_product_catalog()

# create csv file
with open('database.csv', 'w') as csv_file :
  columns = ['Title', 'Price']
  csv_write = writer(csv_file)
  csv_write.writerow(columns)

# get product info and add into csv file
# def get_product_info() :
  for link in catalog :
    request = requests.get(link)
    soup = BeautifulSoup(request.text, 'lxml')

    # set css classes/ids
    target_selector_title = 'line-clamp_root__1FX_J line-clamp_active__Yb_HA'
    target_selector_price = 'price-amount_root__37xv2 product-card-hero-price_now__PlF9u'

    title = soup.find(class_='line-clamp_root__1FX_J line-clamp_active__Yb_HA').get_text().strip()
    price = soup.find(class_='price-amount_root__37xv2 product-card-hero-price_now__PlF9u').get_text().strip()
    print([title, price,])
    csv_write.writerow([title, price,])
