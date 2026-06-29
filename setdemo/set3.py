#if all elements of set1 present in set2 return true otherwise false
s1={1,2,3,4}
s2={1,2,3,4,6,7}
print(s1.issubset(s2))
#if all elements of set2 present in set1 return true otherwise false
print(s2.issuperset(s1))
#isdisjoint true if no commen element in both set
set1={1,2,3}
set2={3,4}
print(set1.isdisjoint(set2))
#intersection update
set11={1,2,3,4}
set12={3,4,5,6}
set11.intersection_update(set12)
print(set11)
set21={1,2,3,4}
set22={3,4,5,6}

set21.difference_update(set22)
print(set21)