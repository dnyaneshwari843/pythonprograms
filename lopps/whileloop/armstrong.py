def ams(num):
    temp=num
    sum=0
    n=len(str(num))
    while num>0:
        d=num%10
        sum=sum+d**n
        num=num//10
    if sum==temp:
        print("armstrong")
    else:
        print("not armstrong")

num=int(input("enter number"))
ams(num)