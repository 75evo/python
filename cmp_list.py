l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
l3=[4,5,6,7,8]

for i in l1:
	for j in l2:
		if i==j:
			print(i,j)

s1=set(l1)
s2=set(l2)
s3=set(l3)
print (s1.intersection(s2,s3))