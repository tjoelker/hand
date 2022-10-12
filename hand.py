import requests
from bs4 import BeautifulSoup
from csv import writer
from lxml import etree

# Get product catalog and append into array.
catalog = []
def get_product_catalog() :
  request = requests.get('https://www.ah.nl/sitemaps/entities/products/detail.xml')
  soup = BeautifulSoup(request.text, 'xml')
  product_catalog = soup.find_all('loc')
  for product in product_catalog :
    catalog.append(product.get_text())

  return catalog

get_product_catalog()

# Create csv file.
with open('database.csv', 'w') as csv_file :
  columns = ['Title', 'Price root', 'Price promo']
  csv_write = writer(csv_file)
  csv_write.writerow(columns)

# Get product info and add into csv file.
  for link in catalog :
    request = requests.get(link)
    soup = BeautifulSoup(request.text, 'lxml')

    # Set css classes/ids.
    target_selector_title = 'line-clamp_root__1FX_J line-clamp_active__Yb_HA'
    target_selector_price_root = 'price-amount_root__37xv2 product-card-hero-price_now__PlF9u'
    target_selector_price_promo_now = 'price-amount_root__37xv2 price-amount_bonus__27nxZ product-card-hero-price_now__PlF9u'
    target_selector_price_promo_prev = 'price-amount_root__37xv2 price-amount_was__1PrUY product-card-hero-price_was__1ZNtq'

    title = soup.find(class_=target_selector_title)
    title = title.get_text().strip()
    price_now = soup.find(class_=target_selector_price_root)
    price_prev = 'null'
    if price_now == None :
      price_now = soup.find(class_=target_selector_price_promo_now)
      price_prev = soup.find(class_=target_selector_price_promo_prev)
    price_now = price_now.get_text().strip()
    if price_prev != 'null' :
      price_prev = price_prev.get_text().strip()
    print([title, price_now, price_prev])
    csv_write.writerow([title, price_now, price_prev])
