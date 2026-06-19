num=int(input("enter number:"))
temp=num
rev=0
for i in range(len(str(num))):
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==temp:
        print("palindrome")
else:
        print("not palindrome")