nestedlist=[[1,2,3],[3,5,6],[7,9,8]]
print("nested list:",nestedlist)
#print first sublist
print("first sublist",nestedlist[0])
element=nestedlist[1][2]
print(element)
#modify element
nestedlist[1][2]=100
print("after modify",nestedlist)
#appending new sublist
nestedlist.append([10,50,60])
print("after appending new sublist",nestedlist)
#extending sublist
nestedlist[3].extend([4,5])
print("after extending element",nestedlist)
#inserting element'
nestedlist[2].insert(3,99)
print("after inserting element",nestedlist)
#removing element
nestedlist[2].remove(99)
print("after removing",nestedlist)
#poping element
pop=nestedlist[1].pop()
print("after popping",nestedlist)
#length of nested list
lengthof=len(nestedlist)
print("length of nested list",lengthof)
