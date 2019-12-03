with open ("random.txt","r") as pf:
 temp=pf.readlines()
 for line in (temp):
     #print (line.upper())
     print (line.isupper())

