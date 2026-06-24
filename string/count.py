def check(str):
    count="i"
    c=0
    for n in str:
        if n==count:
            c+=1
    print(c)
str=input("enter string=")
check(str)   
