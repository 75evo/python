with open ('test.txt','r') as f1:
 foo=f1.read()
 list1=foo.split()
 #print (list1)
 #print(type(list1))
 for i in list1:
  #print(i)
  letters=list(i)
  #print(type(letters))
  #print(letters)
  for j in letters:
   print (j)
   if j.isupper():
    	print("uppercase: " + str(j))
   if j.islower():
    	print("lowercase: " + str(j))
  #print(i)
#list2=['a','b']
  #print(i)
  #list2=list(i)
  #print(list2)
  #list2=[]