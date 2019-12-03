temp=[]
phone_dict={}

def split_phone(phone_list):
    temp=[]
    temp= phone_list.split("-")
    key=temp[0]
    value=temp[1]+temp[2]
    #print(value)
    return key,value

with open ("phone.txt","r") as pf:
    temp=pf.readlines()
    for line in (temp):
        line= line.strip("\n")
        print (line)
        key,value=(split_phone(line))
        print (key,value)
        if key in phone_dict:
            phone_dict[key].append(value)
        else:
            phone_dict[key]=[value]


print (phone_dict)    

