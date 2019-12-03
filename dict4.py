dict1={}


num_stu=int(input("Enter number of students: "))
print(num_stu)

for i in range(0,num_stu):
	stu_name = input("Enter student name: ")
	stu_age = input("Enter student age: ")
	stu_grade = input("Enter student grade: ")
	dict1[stu_name]={stu_age,stu_grade}
print (dict1)
