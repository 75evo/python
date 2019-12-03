s = 'neighneigh'
fw=['n','e','i','g','h']
sound=[]
word=[]
index_word=[]
total = 0
break_flag=0
animal_found=0
animal_index=[]
k=0
j=0
horse=0

for i in range(len(s)):
    sound.append(s[i])
print (sound)

def check_length(fw,sound):
    print (str(sound))
    sound.remove('n')
    print ("Just remove n: " + str(sound))
    if len(fw) > len(sound):
        #return -1
        print (str(len(fw)) + " > " + str(len(sound)))
        exit()
    else:
        print (str(len(fw)) + " < " + str(len(sound)))

def check_prev_horse(animal_index,j):
    prev_horse=1
    print ("check_prev_horse")
    print(len(animal_index))
    if (len(animal_index)==1):
        prev_horse==1
        print("New horse " + str(prev_horse))
        return(prev_horse==1)
    else:
        for a in range(len(animal_index)):
            print ("animal_index: " + str(animal_index[a]))
            if j< (a+4):
                return(prev_horse==1)
                print("Previous horse present, and this could be a new horse")
            else:
                return(prev_horse==0)
                print("Previous horse, no overlapping sound, same horse")

while break_flag==0:
    if animal_found>3:
        exit()
    #for j in range(len(sound)):
    #print("--------------------------------------------------")
    if ((len(sound)) == 0) :
        print (" ***** checking length of temp: ")
        break_flag=1
        break 
    #print("index k: " + str(k))
    target=fw[k]
    list_letter=sound[j]
    #print('target index k=' + str(k) + " " + target + ' ----- list_index j=' + str(j) + " " + list_letter) 
    if list_letter==target:
        print('Letter found!! list_letter: ' + list_letter + ' = target: ' + target) 
        word.append(list_letter)
        #sound.remove(list_letter)
        index_word.append(j)
        k=k+1
        print ("REMOVING letter " + list_letter + " from list ")
        print ("Updated list " + str(sound))
        print ("> > > current word: " + str(word))
        if list_letter=='n':
            print("letter before n: " + str(sound[j-1]) + " - " + str(sound[j]) + " - " + str(sound[j+1]))
            #if sound[j-1]=='x':
            animal_index.append(j)
            horse=check_prev_horse(animal_index,j)
            #print("found n but previous letter was an x")
            print ("%%%%%% First letter of animal sound " + list_letter )
        if str(word)==str(fw):
            print ("Found complete word: " + str(word) + " with fw: " + str(fw) + " index_word: " )
            print ("Clearing word buffer!!!!")
            print ("current status of horse: " + str(horse))
            if (horse==1):
                animal_found=animal_found+1
            print ("animal_found: " + str(animal_found))
            if (len(sound))<(len(fw)):
                break_flag=1
            word=[]
            k=0
        sound[j]='x'
        j=0
        print("Updated list: " + str(sound))
    else:
        j=j+1        
print ("Total animal found: " + str(animal_found))
