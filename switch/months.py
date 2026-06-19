def day():
    while True:
     month=int(input("enter month number from(1,7)"))
     match month:
        case 1:
            print("31 days in january")
        case 2:
            print("29 days in feb")
        case 3:
            print("31 days in march")
        case 4:
            print("30 days")
        case 5:
            print("31 days")
        case 6:
            print("30 days")
        case 7:
            print("31 days")
        case _:
            print("invalid option")
     ch=input("do you want to continue?")
     if ch!='yes' and ch!='YES': 
      break 

day()