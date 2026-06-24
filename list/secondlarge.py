list=[4,45,70,400,23]
largest=list[0]
second=list[0]
for i in list:
    if i >largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print("second largest",second)