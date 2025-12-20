from decimal import Decimal
from gettext import Catalog

catalog = {
    'item_name': 'ChatGPT',
    'version': '4.0',
    'price': Decimal('19.00'),
    'on_sale': True
}


for key in catalog:
    if key == 'on_sale' and catalog[key] == True:
        print(f'{catalog["item_name"]} is currently discounted!')
    elif key == 'on_sale' and catalog[key] == False:
        print(f'{catalog["item_name"]} is at regular price')