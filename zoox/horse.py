x="nneigheigh"
horse_count=0
horse_list=[]
horse_string=""
count=0

for z in x:
    count=count+1
    print ("list z: " + x)
    print ("*** " + str(count) + " foreach z: " + z)
    if z=="n":
        horse_count=horse_count+1
        print("found horse")
        horse_string=z
        print("horse_string " + horse_string)
        print("horse count: " + str(horse_count))
        horse_list.insert(horse_count,horse_string)
        print(horse_list)
    if z=="e":
       print("2 - horse_string " + horse_string)
       if horse_string=="n":
          horse_string=horse_string+z
          print("horse count: " + str(horse_count))
          print ("z==e + " + horse_string)
          horse_list.pop(horse_count-1)
          print("After pop: " + str(horse_list))
          horse_list.insert(horse_count,horse_string)
          print(horse_list)
    if z=="i":
       print("3 - horse_string " + horse_string)
       if horse_string=="ne":
          horse_string=horse_string+z
          print("horse count: " + str(horse_count))
          print ("z==i + " + horse_string)
          horse_list.pop(horse_count-1)
          print("After pop: " + str(horse_list))
          horse_list.insert(horse_count,horse_string)
          print(horse_list)
    if z=="g":
       print("4 - horse_string " + horse_string)
       if horse_string=="nei":
          horse_string=horse_string+z
          print("horse count: " + str(horse_count))
          print ("z==g + " + horse_string)
          horse_list.pop(horse_count-1)
          print("After pop: " + str(horse_list))
          horse_list.insert(horse_count,horse_string)
          print(horse_list)
    if z=="h":
       print("5 - horse_string " + horse_string)
       if horse_string=="neig":
          horse_string=horse_string+z
          print("horse count: " + str(horse_count))
          print ("z==h + " + horse_string)
          horse_list.pop(horse_count-1)
          print("After pop: " + str(horse_list))
          horse_list.insert(horse_count,horse_string)
          print(horse_list)
        #horse_list.append()
    #if i=="e":
    # if (horse_count!=0):
        
