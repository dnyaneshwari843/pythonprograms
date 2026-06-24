year=int(input("enter year to check it is leap year or not:"))
if year%4==0:
    print('leap year')
elif year%400==0:
    print("leap year")
else:
    print('not leap year')
 