
oceans = ["Indian","Pacific","Atlantic","Artic","Southern"]

with open ("oceans.txt","a") as oceans_file:
    for i in oceans:
        oceans_file.write(i+"\n")
    print(oceans,file=oceans_file)
    for i in oceans:
        print(i,file=oceans_file)
