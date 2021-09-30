
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