import array
def searchele(arr,tar):
    for ele in arr:
        return ele
    return -1
arr=array.array('i',[10,20,30,40])
print("array:",arr)
tar=30
result=searchele(arr,tar)
if result!=-1:
    print("number is present")
else:
    print("element is not present")