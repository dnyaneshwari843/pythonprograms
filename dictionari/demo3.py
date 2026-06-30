myd={'a':1,'b':2,'c':3}
print("orignal dictionary",myd)
#add key-value pair
myd['d']=4
print("after adding",myd)
#update value of existing key
myd['b']=50
print("after updating",myd)
#remove key-value pair
del myd['c']
print("after deleting",myd)
#access value by key
a=myd['b']
print("value  of b is",a)
#iterate
for key,value in myd.items():
    print(key,':',value)
#check if key exist
check='e' in myd
print(check)
#get all keys
all=myd.keys()
print("all keys",all)
#get all values
val=myd.values()
print("all values",val)
#get length
print("length of dictionary is",len(myd))
#clear dictionary
myd.clear()
print(myd)
#items method demo
d1={'a':11,'b':22,'c':33}
item=d1.items()
print(item)
#pop item
key,value=d1.popitem()
print(key,value)
print(d1)
#pop method
v=d1.pop('a')
print(v)
print(d1)
#update
d1.update({'ab':22,'c':44})
print(d1)