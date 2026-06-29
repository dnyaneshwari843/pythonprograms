list=[23,21,10,70,60]
large=list[0]

second=list[0]
for i in list:
     if i>large:
         largest=i
for i in list:
    if i>second and i!=large:
        second=i
print('second largest element is',second)

