uppercase=0
lowercase=0
result_dict={'Lowercase':0,'Uppercase':0}
with open("test.txt",'r') as file1:
 list1 = file1.read()
 for i in list1:
 	if i.islower():
 		lowercase+=1
 		result_dict['Lowercase']+=1
 	elif i.isupper():
 		uppercase+=1
 		result_dict['Uppercase']+=1
 print(uppercase,lowercase)
 print(result_dict)