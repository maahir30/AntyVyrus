
'''
import requests as requests
import simplejson as json

API_Key = "tDEHxW_Jr1TW"
Project_Token = "tENR1ercxLe"
Run_Token = "tU7b3K0S4pyz"

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{Project_Token}/last_ready_run/data', params=API_Key)
data = json.loads(response.text)
print(data)
'''

'''
import requests
import json
import pyttsx3
import speech_recognition as sr
import re
import threading
import time
'''
import requests
import json

API_KEY = "tDEHxW_Jr1TW"
PROJECT_TOKEN = "tENR1ercxLe_"
RUN_TOKEN = "tU7b3K0S4pyz"


def main(text):

	class Data:
		def __init__(self, api_key, project_token):
			self.API_Key = api_key
			self.Project_Token = project_token
			self.params = {
				"api_key": self.API_Key
			}
			self.data = self.get_data()

		def get_data(self):
			response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.Project_Token}/last_ready_run/data', params=self.params)
			data = json.loads(response.text)
			return data

		def get_country_info(self, country):
			data = self.data["country"]

			for content in data:
				if content['name'].lower() == country.lower():
					return content

			return "0"

		def get_list(self):
			countries = []
			for country in self.data['country']:
				countries.append(country['name'].lower())

			return countries

	data = Data(API_KEY, PROJECT_TOKEN)


	def return_data(country):
		country_stuff = data.get_country_info(country)
		country_stuff = data.get_country_info(country)
		cases = (country_stuff['total_cases'])
		deaths = (country_stuff['total_deaths'])
		return cases, deaths



	data = Data(API_KEY, PROJECT_TOKEN)
	#print(data.get_data())

	user_country = text


	cases_deaths = return_data(user_country)
	return cases_deaths



if __name__ == "__main__":
	main()



