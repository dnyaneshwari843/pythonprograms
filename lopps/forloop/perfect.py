def perfect(num):
 p=0
 for i in range(1,num//2+1):
    if num%i==0:
        p+=i
 if p==num:
    print(f"{num} is perfect number")
 else:
    print(f"{num} is not perfect number")
perfect(6)









