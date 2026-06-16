n=int(input("enter number:"))
a,b=0,1

for i in range(n):
    print(a, end=" ")
    a,b=b,a+b
    
#java
f=0
s=1
print(f,end=" ")
print(s,end=" ")
for i in range(2,n):
    t=f+s
    print(t)
    f=s
    s=t