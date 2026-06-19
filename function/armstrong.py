def ams(num):
    temp=num
    sum=0
    n=len(str(num))
    for i in range(n):
        d=num%10
        sum=sum+d**n
        num=num//10
    if sum==temp:
        print("armstrong")
    else:
        print("not armstrong")

num=int(input("enter number"))
ams(num)
        








