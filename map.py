import functools

def map_test (lst1):
    lst2=[]
    for i in lst1:
        lst2.append(i**2)
    return lst2

print (map_test([1,2,3,4]))

n=[4,3,2,1]
print(list(map(lambda x:x**2,n)))
print (list(filter(lambda x:x>2,n)))
print (functools.reduce(lambda x,y:y*x,n))
#print(list(map(map_test,n)))
