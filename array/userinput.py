
def user_input():
    n=int(input("enter the number of elements in the array:"))
    arr=[]
    for i in range(n):
        ele=int(input(f"enter enter {i+1}:"))
        arr.append(ele)
    print(arr)
    for num in arr:
        if num%2==0:
            print("even =",num,end=" ")
         
        
        

user_input()