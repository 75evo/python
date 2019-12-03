
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list)

list1=[5,4,7]
final_list2 = list(map(lambda x: x*2,list1))
print(final_list2)