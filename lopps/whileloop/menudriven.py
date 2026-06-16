def calculator():
    while True:
        print("simple calculator menu:")
        print("1. cube of a number")
        print("2. square of a number")
        print("3. sum of digit")
        print("4.prime number")
        print("5.exit")
        choice=input("enter your choice(1-4):")
        if choice=='5':
            print("existting the calculator.Goodbye")
            break
        num=int(input("enter a   number="))
        if choice=='1':
            result=num**2
            print(f"the square of {num} is:{result}")
        elif choice=='2':
            result=num**3
            print(f"the cube of {num} is:{result}")
        elif choice=='3':
            sum=0
            temp=num
            while num>0:
              d=num%10
              sum+=d
              num//=10
            print(f"sum of {temp} is:{sum}") 
        elif choice=='4':
            if num <=1:
               print("enter  positive number")
            else:
             count=0
            for i in range(2,num//2+1):
               if num%i==0:
                count+=1

               print("count",count)
               if count==0:
                 print("prime number")
               else:
                  print("not prime number")
        else:
            print("invalid choice.please select valid option")
calculator()