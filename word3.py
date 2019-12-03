s = 'nneigheigh'
fw=['n','e','i','g','h']
sound=[]
word=[]
index_word=[]
total = 0
break_flag=0
animal_found=0
k=0
j=0

for i in range(len(s)):
    sound.append(s[i])
print (sound)

while break_flag==0:
    #for j in range(len(sound)):
    print("--------------------------------------------------")
    if ((len(sound)) == 0) :
        print (" ***** checking length of temp: ")
        break_flag=1
        break 
    print("index k: " + str(k))
    target=fw[k]
    list_letter=sound[j]
    print('target index k=' + str(k) + " " + target + ' ----- list_index j=' + str(j) + " " + list_letter) 
    if list_letter==target:
        print('Letter found!! list_letter: ' + list_letter + ' = target: ' + target) 
        word.append(list_letter)
        sound.remove(list_letter)
        index_word.append(j)
        k=k+1
        print ("REMOVING letter " + list_letter + " from list ")
        print ("Updated list " + str(sound))
        #print ("Index 0 now at " + str(sound[0]))
        print ("> > > current word: " + str(word))
        j=0
        if list_letter=='n':
            print ("%%%%%% First letter of animal sound " + list_letter)
        if str(word)==str(fw):
            print ("Found complete word: " + str(word) + " with fw: " + str(fw) + " index_word: " + str(index_word))
            print ("Clearing word buffer!!!!")
            animal_found=animal_found+1
            print ("animal_found: " + str(animal_found))
            if (len(sound))<(len(fw)):
                break_flag=1
            word=[]
            k=0
            #break
        #print('i : ' + str(i) + ' j : ' + str(j) + ' word: ' + str(word)) 
        #print("length of temp: " + str(len(temp)) + " " + str(temp))
    else:
        j=j+1        
print ("Total animal found: " + str(animal_found))
