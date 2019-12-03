friends = ["Jim" , "Jane" , "Joe"]

for index in range(len(friends)):
    print (friends[index])



try: 
    #value = 10/0
    number = int(input("Enter a number: " ))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")
