num=[1,2,3,4,5]
sq=list(map(lambda x:x**2,num))
print(sq)
#even number
even=list(filter(lambda x:x%2==0,num))
print(even)
#sort list
sort=sorted(num,key=lambda x:-x)
print(sort)