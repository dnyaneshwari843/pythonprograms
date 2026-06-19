def calculator():
    while True:
        print("simple calculator menu:")
        print("1. add")
        print("2. sub")
        print("3. multi")
        print("4.div")
        print("5.exit")
        choice=int(input("enter your choice(1-4)"))
        if choice=="5":
          print("exit")
          break
        n1=int(input("enter first number:"))
        n2=int(input("enter second number:"))
        match choice:
              case 1:
               print("addition=",n1+n2)
              case 2:
               print("substraction=",n1-n2)
              case 3:
               print("multiplication=",n1*n2)
              case 4:
               print("division=",n1/n2)
              case _:
               print("invalid option")
        ch=input("do you want to continue?(yes/no)")
        if ch!="yes":
          break
calculator()      
        
            