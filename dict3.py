thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for key,val in thisdict.items():
  print(key,val)

if "model" in thisdict:
	print("model exists")

print (len(thisdict))

thisdict["brand"]="kooster"
print(thisdict)
