import array
def reverse(arr):
    n=len(arr)
    for i in range(n//2):
        arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
    return arr    
arr=[5,8,9,6,2]
print("orignal array=",arr)
reverse(arr)
print("reverse array=",arr)

