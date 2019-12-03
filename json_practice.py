import json

final_list=[]

def get_user_names():

	question_access = read_content['results']
	for question_data in question_access:
		replies_access = question_data['replies']
		for replies_data in replies_access:
			user_name = replies_data['user']['display_name']
			print(user_name)
			final_list.append(user_name)
			print(final_list)

with open ('test3.json','r') as fjson:
	read_content=json.load(fjson)
	#print(type(read_content))
	#question_access = read_content['results']
	#print(question_access)
	#print(type(question_access))
	#for question_data in question_access:
	#	print(question_data)
	#print(type(question_data))
	#replies_access = question_data['replies']
	#print(replies_access)
	#print(type(replies_access))
	#for replies_data in replies_access:
	#	print(replies_data)
	#user_name = replies_data['user']['display_name']
	#print(user_name)
get_user_names()

with open ('output.json','w') as fjson2:
	json.dump(final_list,fjson2)



