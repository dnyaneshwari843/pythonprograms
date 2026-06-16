def suofdmax(num):
 sum=0
 max=0
 for i in range(len(str(num))):
    
    dig=num%10
    if dig>max:
     max=dig
    print("maximum number is",max)
    sum+=dig
    num=num//10
    print(f"sum of {sum} is",sum)
num=int(input("enter number:"))
suofdmax(num)