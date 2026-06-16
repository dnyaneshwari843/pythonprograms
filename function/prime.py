def prime(num):
    if num<=1:
        print("not prime")
    else:
        count=0
        for i in range(2,num//2+1):
            if num%i==0:
                count+=1
        #print("count:",count)
        if count==0:
            print(f"prime number ={num}")
            
#num=int(input("enter number:"))
#prime(num)
def tocheck():
    print("prime number from 1 to 100")
    for num in range(1,101):
        prime(num)
        
tocheck()

