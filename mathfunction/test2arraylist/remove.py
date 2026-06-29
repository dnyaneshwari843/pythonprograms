list=[10,67,10,67,67,4,5]
new=[10,67]
for i in list:
    if i not  in new:
        new.append(i)
print(new)