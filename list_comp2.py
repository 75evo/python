l1=[1,2,3,4,5]
l2=list([x**2 for x in l1])
print(l2)

l3=[1,2,3,4,5]
l4=[3,4,5,6,7]
set1=set(l3)
set2=set(l4)
set3=set1.intersection(set2)
print(set3)