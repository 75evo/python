
from math import *

phrase = "chicken little"
print(phrase.index("l"))
print(phrase.replace("little","chicken"))
print(phrase[3])

my_num = -5
print(min(3,7))
print(round(3.7))

def sayhi(name="James", age=25):
    print("hello" + name + " you are " + str(age))


sayhi("John",33)
sayhi()

def my_gender(gender="male"):
        gender=gender.lower()
        if gender=="male":
            print("John")
        elif gender=="female":
            print("Jane")

my_gender("FEMALE")

i=1
while i <= 10:
    print ("while loop " + str(i))
    i += 1

password = "test"
guess = ""
guess_count = 0

while guess != password :
    guess = input("Enter password: ")
    guess_count = guess_count + 1   
    if (guess_count > 0) and (guess_count < 3):
        print ("wrong password!" + str(guess_count))
    elif (guess_count >= 3):
        print ("wrong password! Number of tries exceeded")
        exit()

print ("You now have access!")
