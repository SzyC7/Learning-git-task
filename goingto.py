print("shopping list")
shopping_list = {'Bakery': ('bread', 'buns', 'donuts'),
'Greengrocers' : ('carrots', 'beetroots', 'potatoes')}

for shop, products in shopping_list.items():
    print('Going to', shop, 'and buying', products)