def reverse_vowels(word):
    
    vowels_list=[]
    consonant_list=[]
    vowels=["a","e","i","o","u"]
    index=[]
    temp_word=[]
    index=0
    
    if len(word)==0: #exit if 0 length word
        return False
    
    for i in word:
        if " " == i:
            print (word + " not supported. Single words only, no blank spaces or phrases")
            return False
        if i in vowels:
            vowels_list.append(i)
            temp_word.append("")
        else:
            consonant_list.append(i) #create consonant list, not really necessary
            temp_word.append(i) 

    vowels_list.reverse() #reverse vowel list
    
    for j in temp_word:
        if j=='':           
            temp_word.insert(index,vowels_list[0]) #create temp word, insert reverse vowel list 0th element
            temp_word.pop(index+1) #pop the blank space
            vowels_list.pop(0) #pop the inserted vowel from the vowel list 
        index+=1 

    new_word="".join(temp_word) #create new word
    return new_word

print(reverse_vowels("aa parameter"))
print(reverse_vowels("hkkkkjjjja;ill"))
print(reverse_vowels("aaaaeeeuuu"))