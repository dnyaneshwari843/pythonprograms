#To check given number is perfect or not
def perfect(num):
    i=1
    sum=0
    while i<num//2+1:
        if num%i==0:
            sum+=i
        i+=1
    if sum==num:
     print(f"{num} is perfect number")
    
    else:
      print(f"{num} is not perfect number")

#for n in range(1,100):
perfect(56)