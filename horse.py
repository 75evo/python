def horse(n):
    word='neigh'
    word_dic={}.fromkeys(word,0)
    print(word,word_dic)
    for i in n:
        print (i)
        if i in word:
            word_dic[i]+=1
    print(word_dic['n'])


horse('nneigheighneigh')
