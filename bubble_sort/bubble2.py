orig=[1,5,7,2,3,1,10,122,4]
counter=0
#for i in orig:
print (orig)

print ("sorting")

list_len=len(orig)
print("list length: " + str(list_len))
#print (str(orig[1]))

#pre opt
if orig[list_len-2]>orig[list_len-1]:
    temp=orig[list_len-2]
    orig[list_len-2]=orig[list_len-1]
    orig[list_len-1]=temp
print(orig)
for x in range(0,list_len-1):
 print("new iteration")
 print(orig)
 for x in range(0,list_len-1):
  print (str(orig[x]))
  if orig[x]>orig[x+1]:
     print ("comparing " + str(orig[x]) + " to " + str(orig[x+1]) + " : bigger than, going to switch")
     temp=orig[x]
     orig[x]=orig[x+1]
     orig[x+1]=temp
  if (orig[x]<orig[x+1]) or (orig[x]==orig[x+1]):
     print ("comparing " + str(orig[x]) + " to " + str(orig[x+1]) + " : smaller than or equal to. Do nothing")
  counter=counter+1

print ("counter: " + str(counter))
print (orig)
