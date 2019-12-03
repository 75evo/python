try:
    with open("arandom.txt") as random_file:
    #print(random_file.readable())
    #print(random_file.readlines())
        for line in random_file:
            line.strip()
            print (line)
except FileNotFoundError:
    text = None
