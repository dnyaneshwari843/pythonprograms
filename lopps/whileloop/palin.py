def pali(num):
  temp=num
  rev=0
  while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
  if rev==temp:
        print("palindrome")
  else:
        print("not palindrome")
num=int(input(f"enter number to check it is palindrome or not:"))
pali(num)