#the number which is divisible by 3 and 5
def check(num):
    i=1
    while i<=num:
        if i%3 == 0 and i%5 == 0:
            print(i,end=" ")
        i += 1
check(20)