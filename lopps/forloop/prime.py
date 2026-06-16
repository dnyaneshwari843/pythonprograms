num=50
if num <=1:
    print("enter  positive number")
else:
    count=0
    for i in range(2,num//2+1):
        if num%i==0:
         count+=1

        
    if count==0:
            print("prime number")
    else:
            print("not prime number")