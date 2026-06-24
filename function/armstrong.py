def ams(num):
    temp=num
    sum=0
   
    for i in range(len(str(num))):
        d=num%10
        sum=sum+d**3
        num=num//10
    if sum==temp:
        print("armstrong")
    else:
        print("not armstrong")

num=int(input("enter number"))
ams(num)
        








