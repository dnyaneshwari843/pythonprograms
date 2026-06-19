def calculator(value):
    n1=int(input("enter first number:"))
    n2=int(input("enter second number:"))
    match value:
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
calculator(5)      