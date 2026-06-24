def sort(list):
    n=len(list)
    for i in range(n):
        for j in range(0,n-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list
list=[97,56,45,23,11,0]
print("orignal list",list)
sort(list)
print("sorted list",list)
print("second highest element is",list[-2])