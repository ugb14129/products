
products = []

while True:
	name = input('Please enter product name: ')
	if name == 'q':
		break
	price = input('Please enter product price: ')	
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)
	products.append([name, price])

print(products)		

for p in products:
	print(p[0], 'price is ', p[1])


with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('products 商品,price 价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') 