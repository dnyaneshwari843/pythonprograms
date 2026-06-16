def ams(num):
    temp=num
    sum=0
    n=len(str(num))
    while temp>0:
        d=temp%10
        sum=sum+d**n
        temp=temp//10
    if sum==num:
        print("armstrong")
    else:
        print("not armstrong")

num=int(input("enter number"))
ams(num)