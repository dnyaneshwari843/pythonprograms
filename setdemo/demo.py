set={1,2,3,4,5}
print("initial set:",set)
#add element
set.add(6)
print("after adding 6:",set)
#remove element
set.remove(4)
print("set after removing 4",set)
#discard element
set.discard(10)
print("set after discarding",set)
#update set with multiple element
set.update([7,8,9,7,4])
print("set after updating",set)
#pop element
set.pop()
print("after popping element",set)
#use membership operator
print("4 in my set",4 in set)
#set opration
set1={1,5,6}
set2={3,5,0}
setunion=set1 | set2
print(setunion)

#intersection
inter=set1 & set2
print(inter)
#difference
#find ele in set1 not in set2
diff=set1-set2
print(diff)
#semmetric difference
sys=set1^set2
print(sys)
#clear set
set.clear()
print(set)
#copy set
setc=set1.copy()
print(setc)