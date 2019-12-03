A="nneigheigh"
#A="neigh"
neigh = "neigh"

#create a dictionary for position and enumate the word neigh
letter_dict = {v: k for k, v in enumerate(neigh)}
print (letter_dict)

#create a list for letter positions
position = [0] * (len(neigh) + 1)
print ('postion: ' + str(position))

maxH = curH = 0

for i in range(len(A)):
    print('----------------------------------------')
    print ("index i: " + str(i))
    #check if the first letter of dict matches first letter of string A
    print ("value: " + str(letter_dict[A[0]]))
    print ("mod len A len neigh: " + str(len(A)%len(neigh)))
    print ("Get letter_dict: " + str(letter_dict.get(A[i],-1)))
    if(letter_dict[A[0]] !=0 or len(A) % len(neigh) != 0 or letter_dict.get(A[i],-1) == -1):
        print ("-1")
    print ("letter position: " + str(letter_dict[A[i]]))
    pos = letter_dict[A[i]]
    print("Position: " + str(pos))
    if(pos == 0):
        curH +=1
        print("curH: " + str(curH))
        maxH = max(maxH, curH)
        position[0] += 1
        print("Position: " + str(position[0]))
    else:
        if(position[pos -1] == 0):
            print("Position - 1 : " + str(position[0]))
            print ("-1")
        position[pos -1]-=1
        if(pos == (len(neigh) - 1)):
            curH -=1
        else:
            position[pos]+=1
for i in range(len(position)):
    if(position[i] == 1): 
        print ("-1")
print (maxH)
