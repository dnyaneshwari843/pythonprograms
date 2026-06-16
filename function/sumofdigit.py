def sod(num):
    sum=0
    for i in range(num):
        d=num%10
        sum+=d
        num//=10
    return sum
num=int(input("enter number"))

print(f"the sum of digit is:{sod(num)}")