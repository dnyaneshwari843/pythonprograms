import array
def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
arr=[15,5,87,43] 
print("orignal array",arr)
sorted=sort(arr)
print("sorted array",sorted)
        