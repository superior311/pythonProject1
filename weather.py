import requests
import json


def print_weather(city):
	url = "https://api.weatherbit.io/v2.0/current"
	params = {"city": city, "key": "1ab5e9499298416b97674b2facdaeb1c"}
	output = requests.get(url, params)
	body = json.loads(output.content)
	# print(body)
	data = body['data'][0]
	print('clouds' + str(data['clouds']))
	print('description: ' + data['weather']['description'])
	print('app temp : ' + str(data['temp']) + 'C')


print_weather('New York,NY')
