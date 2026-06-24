#print orignal list
list=[1,60,67,90]
print("orignal list=",list)
#append method
list.append(91)
print("after appending one element",list)
#extend method
list.extend([20])
print("after extendig",list)
#insrt method
list.insert(0,10)
print("after insert",list)
#remove method
list.remove(10)
print(list)
#pop method
list.pop()
print(list)
#clear method
list.clear()
print("after clearing list",list)
list=[90,78,56,32,90]
#index method
index=list.index(90)
print("the index of element",index)
#index with start and end
index=list.index(78,0,4)
print(index)
#count method
count=list.count(90)
print(count)
#sort
list.sort(reverse=False)

print(list)
#reverse method
list.reverse()
print("after reverse",list)

#copy method
copy=list.copy()
print(copy)
#length of list
length=len(list)
print("length of list",length)
#demostrating slicing
sliced=list[1:4]
print("after slicoing",sliced)
#demostrating conacatination
list1=list+[10,60,70]
print(list1)
#demostrating repitation
repeat=list*2
print(repeat)
#demostrating membership
check=90 in list
print(check)
#demostating iteration
for i in list:
    print(i)
#max and min 
max=max(list)
min=min(list)
print("maximum value",max)
print("minimum value",min)
#sum function
sum=sum(list)
print("sum is",sum)