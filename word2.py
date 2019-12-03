s = 'worrofwoof'
fw=['w','o','o','f']
temp=[]
word=[]
total = 0
break_flag=0
animal_found=0
for i in range(len(s)):
    temp.append(s[i])
print (temp)

while break_flag==0:
    for i in range(len(fw)):
        print("--------------------------------------------------")
        target=fw[i]
        if (len(temp)) < 4:
            print (" ***** checking length of temp: ")
            break_flag=1
            exit() 
        #print('i : ' + str(i)) 
        for j in range(len(s)):
            list_letter=temp[j]
            print('target index i : ' + str(i) + " " + target + ' ----- list_index j : ' + str(j) + " " + list_letter) 
            if list_letter==target:
                print('Letter found!! list_letter: ' + list_letter + ' = target: ' + target) 
                word.append(target)
                temp.remove(list_letter)
                print ("REMOVING letter " + target + " from list " + str(temp))
                print ("--------current word: " + str(word))
                if target=='w':
                    print ("%%%%%% First letter of animal sound " + target)
            pass
            if str(word)==str(fw):
                print ("Found complete word: " + str(word) + " with fw: " + str(fw))
                print ("Clearing word buffer!!!!")
                animal_found=animal_found+1
                print ("animal_found: " + str(animal_found))
                word=[]
                print (temp)
            #break
        print('i : ' + str(i) + ' j : ' + str(j) + ' word: ' + str(word)) 
        print("length of temp: " + str(len(temp)) + " " + str(temp))
        
print ("after pop: " + str(temp))
