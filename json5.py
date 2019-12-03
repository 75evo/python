import json
list2=[]
with open ('test3.json','r') as fj:
	data = json.load(fj)
	print(type(data))
	results=data['results']
	print(results)
	print(type(results))
	for classes in results:
		print (classes)
		print(type(classes))
		replies=classes['replies']
		print (replies)
		print(type(replies))
		for user in replies:
			print (user)
			print(type(user))
			name=user['user']['display_name']
			print(name)
			list2.append(name)
print (list2)

with open ('data3.json','w') as fj2:
	json.dump(list2,fj2)


