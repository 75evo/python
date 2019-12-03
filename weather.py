import requests
import json

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=4864b08f0eff7c8e5f4c17b1423dbbbc&zip='
city = '94086'
url = api_address + city

json_data = requests.get(url).json()

print(json_data)

#data2=json.dump(requests.get(url).json())

formatted_data = (json_data['weather'][0]['description'])
print(formatted_data)
