def max(arr):
    max=arr[0]
    min=arr[0]
    for i in arr:
        if i>max:
            max=i
        if i<min:
            min=i
    print("max number is=",max)
    print("min number is=",min)
arr=[12,14,86,1,100]
max(arr)