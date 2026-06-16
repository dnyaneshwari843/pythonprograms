def palin(num):
    temp=num
    sum=0
    n=len(str(num))
    for i in range(n):
        d=num%10
        sum=sum*10+d
        num=num//10
    if sum==temp:
        print(f"{temp} is palindrome")
    else:
        print(f"{temp} is not palindrome")

num=int(input("enter number:"))
palin(num)