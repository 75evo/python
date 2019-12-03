import json
import requests

payload={'page':2,'count':25}
payload2={'username':'corey','password':'testing'}
request = requests.post("https://httpbin.org/post",data=payload2)
#print(request.json())
print(request.json)
#text_data = request.text
#print(type(text_data.text))
#dict1=json.dump(text_data)
#print(type(dict1))
#json.loads(request)
#print(dict1)