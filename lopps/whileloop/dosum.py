def dosum():
    sum=0
    while True:
        num=int(input("enter a number to add to the (0 to stop):"))
        if num == 0:
            break
        sum+=num
    return sum
print("the taotal sum is ",dosum())