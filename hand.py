import requests
from bs4 import BeautifulSoup
from csv import writer

request = requests.get('https://www.ah.nl/producten/frisdrank-sappen-koffie-thee')

soup = BeautifulSoup(request.text, 'html.parser')

products = soup.find_all(class_='product-card-portrait_root__sZL4I product-grid-lane_gridItem__eqh9g')

with open('database.csv', 'w') as csv_file:
  csv_writer = writer(csv_file)
  collumns = ['Title', 'Price']
  csv_writer.writerow(collumns)

  for product in products:
    title = product.find(class_='line-clamp_root__1FX_J line-clamp_active__Yb_HA title_lineclamp__1dS7X').get_text().strip()
    price = product.find(class_='price-amount_root__37xv2 price-amount_highlight__3WjBM price_amount__2Gk9i price_highlight__3B97G').get_text().strip()
    print([title, price,])
    csv_writer.writerow([title, price,])