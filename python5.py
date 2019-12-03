import re

my_string="Hello there"

if my_string.find("th") !=-1:
    print ("x")
if "th" in my_string:
    print("found")

pattern=re.compile("please")

with open ("random.txt","r",encoding="utf-8") as f:
    contents=f.read()

    matches=pattern.finditer(contents)
    for match in matches:
        print(match)
