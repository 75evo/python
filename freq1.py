line='This is just a test. This is not a bad test, just a small test'
word_dict={}
word_dict2={}
for word in line.split():
	#print (word)
	if word in word_dict:
	 word_dict[word]+=1
	else:
	 word_dict[word]=1
	#print(word_dict)

for word in line.split():
	word_dict2[word]=word_dict2.setdefault(word,0)+1

print(word_dict2)
