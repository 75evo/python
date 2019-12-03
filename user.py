user_dict={}
with open ('users.csv','r') as f1:
	data=f1.readlines()
	print(data)
	for person in data:
		print(person)
		x=person.split(',')
		print(x)
		if ('name' in x):
			pass
		else:
			user_dict[x[0]]={x[1],x[2]}
print(user_dict)


