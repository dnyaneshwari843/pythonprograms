def sod(num):
    sum=0
    temp=num
    while num>0:
        d=num%10
        sum+=d
        num//=10
        
    print(f"sum of {temp} is:{sum}") 
      
num=int(input("enter number="))
sod(num)