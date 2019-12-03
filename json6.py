#import json
import urllib
print(dir(urllib))
from urllib import request
print(dir(request))
#.request import request

#with urlopen("https://www.wikipedia.org") as response:
#    source = response.read()

#print(source)
#print(type(source))


resp= request.urlopen("https://www.wikipedia.org") 
print(type(resp))
print(resp.code)
data=resp.read()
print(type(data))
print(len(data))
html=data.decode("UTF-8")
print(type(html))
print(html)
print(resp.read())