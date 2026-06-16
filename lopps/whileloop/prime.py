def prime(num):
    i=2
    if num <=1:
     print("enter  positive number")
    else:
     count=0
    while i<=num//2+1:
        if num%i==0:
            count+=1
    if count==0:
            print("prime number")
    else:
            print("not prime number")
num=int(input("enter number"))
prime(num)