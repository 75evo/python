import os

list=[1,2,3,4,5]

my_list=[n*n for n in list]

print (my_list)
spath="/Users/zamanizambri/scripts"
print (os.listdir(spath))

for roots, dirs, files in os.walk(spath):
    print ("file: %s" % files)
    print ("dir: %s" % dirs)


