#accept the bike price from user & add road tax as follows
price=int(input('enter the price of bike'))
if price>80000:
    print('15% tax')
elif price>40000 and price<80000:
    print('10% tax')
else:
    print('5% tax')
    