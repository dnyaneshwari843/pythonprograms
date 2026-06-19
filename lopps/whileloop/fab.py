def fabo(num):
    a,b=0,1
    i=0
    while i<num:
        print(a,end="  ")
        a,b=b,a+b
        i+=1
num=int(input("enter number:"))
fabo(num)