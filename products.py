import os # operating system

def read_file(filename):
	products = []
			
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'products 商品,price 价格' in line:
				continue
			name , price = line.strip().split(',')
			products.append([name, price])
	return products	


# read file



# Enter data
def user_input(products):
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
	return products


# Print all data
def print_products(products):
	for p in products:
		print(p[0], 'price is ', p[1])


# Write Data
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('products 商品,price 价格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') 


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('Yes, Found it')
		products = read_file(filename)
	else:
		print('Nah, cannot find it')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)		

main()	