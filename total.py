print("shopping list")
shopping_list = {'Bakery': ('bread', 'buns', 'donuts'),
'Greengrocers' : ('carrots', 'beetroots', 'potatoes')}

for shop, products in shopping_list.items():
    print('Going to', shop, 'and buying', products)

res = {key: [ele.capitalize() for ele in shopping_list[key] ] for key in shopping_list}
print("Lista produktów po powiększeniu liter" + str(res))


for products in shopping_list:
    print('In total I am buying', len(products), 'products')
    break