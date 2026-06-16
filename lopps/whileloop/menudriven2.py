def calculator():
    while True:
        print("simple calculator menu:")
        print("1. to check number is even or odd")
        print("2. to check number is armstrong or not")
        print("3. to check number is palindrome or not")
        print("4. to check number is perfect or not")
        print("5.exit")
        choice=input("enter your choice(1-4):")
        if choice=='5':
            print("existting the calculator.Goodbye")
            break
        num=int(input("enter a   number="))
        if choice=='1':
            if num%2==0:
              print('enter no is even')
            else:
               print('enter no is odd')
        if choice=='2':
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
        if choice=='3':
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
        if choice=='4':
           i=1
           sum=0
           while i<num//2+1:
             if num%i==0:
              sum+=i
             i+=1
           if sum==num:
             print(f"{num} is perfect number")
    
           else:
             print(f"{num} is not perfect number")
        else:
            print("invalid choice.please select valid option")
calculator()