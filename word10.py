

s = 'neighneigh'


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
        return(prev_horse==1)
    else:
        for a in range(len(animal_index)):
            if j< (a+4):
                return(prev_horse==1)
            else:
                return(prev_horse==0)



def solve(self,A)
    sound=[]
    word=[]
    index_word=[]
    total = 0
    animal_found=0
    animal_index=[]
    k=0
    j=0
    horse=0
    fw=['n','e','i','g','h']


    for i in range(len(s)):
        sound.append(s[i])
        #print (sound)

    while j<len(sound):
        target=fw[k]
        list_letter=sound[j]
        if list_letter==target:
            #print('Letter found!! list_letter: ' + list_letter + ' = target: ' + target) 
            word.append(list_letter)
            index_word.append(j)
            k=k+1
            if list_letter=='n':
                animal_index.append(j)
                horse=check_prev_horse(animal_index,j)
            if str(word)==str(fw):
                if (horse==1):
                    animal_found=animal_found+1
                if (len(sound))<(len(fw)):
                    break_flag=1
                word=[]
                k=0
            sound[j]='x'
            j=0
        else:
            j=j+1        
    print ("Total animal found: " + str(animal_found))
    return (animal_found)
