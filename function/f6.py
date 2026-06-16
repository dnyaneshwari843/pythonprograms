def multiply(*args):
    result=1
    for num in args:
        result *=num
    return result
print(f"multiplication of 5,6,7,8,9 is:{multiply(5,6,7,8,9)}")
print(f"multipply of 10,10 is:{multiply(10,10)}")