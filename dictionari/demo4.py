d1={'a': 22, 'b': 22, 'c': 44}
keys=('a','b','c')
dv=0
myd=d1.fromkeys(keys,dv)
print(myd)
#set default method
v=myd.setdefault('d',4)
print(v)
print(myd)
val=myd.get('e','not found')
print(val)
print(myd)