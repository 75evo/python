def dup(list1):
 non_dup = []
 temp = []
 print (list1)
 for x in list1:
  if x not in temp:
   temp.append(x)

 print(temp)
 return(len(temp))

print(dup([1,1,2]))
