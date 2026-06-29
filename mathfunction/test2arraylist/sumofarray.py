import array
def sum(arr):
    sum=0
    for i in arr:
        sum+=i
    print("sum is",sum)
arr=array.array('i',[1,2,3,5,8])
sum(arr)