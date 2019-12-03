
stu_num=int(input("number of student"))
print(stu_num)
stu_dict={}


for i in range (0,stu_num):
 stu_name=input("enter student name: ")
 stu_age=input("enter student age: ")
 stu_grade=input("enter student grade: ")
 stu_dict[stu_name]={stu_age,stu_grade}

print(stu_dict)