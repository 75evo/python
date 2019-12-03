record = int(input("Enter the student record need to add :"))
print("record: " + str(record))
stud_data={}
for i in range(0,record):
    Name = input("Enter the student name :")#.split()
    Age = input("Enter the {} age :".format(Name))
    Grade = input("Enter the {} grade :".format(Name))#.split()
    Nam_key =  Name
    Age_value = Age
    Grade_value = Grade
    stud_data[Nam_key] = {Age_value,Grade_value}

print(stud_data)