year=int(input("enter year:"))
for i in range(year):
    if year%4==0:
        print("leap year")
    else:
        print("not leap year")