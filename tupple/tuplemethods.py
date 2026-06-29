#length of tuple
t=(2,6,90,60)
print("length of tuple is=",len(t))
#access element
print("accesing element at index 2=",t[2])
#tuple slicing
print('slicing element from index 1 to 4=',t[1:4])
#concate tuple
t2=t+('a','h')
print("after concate=",t2)
#repeat 
t3=t*3
print("after reapiting=",t3)
#index
print("index of element",t.index(2))
#count
cnt=t.count(2)
print("count of element is",cnt)