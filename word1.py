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
    for i in range(len(s)):
        if (len(temp)) < 4:
            print (" ***** checking length of temp: ")
            break_flag=1
            exit() 
        print('i : ' + str(i)) 
        print('* list letter: ' + temp[i])
        for j in range(len(fw)):
            print('i : ' + str(i) + ' j : ' + str(j) ) 
            find_letter=fw[j]
            print('find letter: ' + find_letter)
            if temp[i]==find_letter: 
                print('Letter found!! list_letter: ' + temp[i] + ' = find_letter: ' + find_letter) 
                if find_letter=='w':
                    print ("possible horse: " + str(temp[i]))
                temp.remove(find_letter)
                print ("REMOVING letter " + find_letter)
            print("length of temp: " + str(len(temp)) + " " + str(temp))
            word.append(find_letter)
            print ("current word: " + str(word))
        #print('i : ' + str(i) + ' j : ' + str(j) + ' word: ' + str(word)) 
            if str(word)==str(fw):
                print ("Found complete word: " + str(word) + " with fw: " + str(fw))
                print ("Clearing word buffer!!!!")
                animal_found=animal_found+1
                print ("animal_found: " + str(animal_found))
                word=[]
                print (temp)
            #break
        print('i : ' + str(i) + ' j : ' + str(j) + ' word: ' + str(word)) 
        
print ("after pop: " + str(temp))
