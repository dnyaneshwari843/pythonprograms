def check(str):
    vowels="aeiouAEIOU"
    count=0
    for  i in str:
        if i in vowels:
            print(i)
            count+=1
    print(count)
str=input("enter string")
check(str)