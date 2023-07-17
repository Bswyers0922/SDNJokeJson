import requests
import json

url = "https://icanhazdadjoke.com/"

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

jokeJson = response.json()

joke=jokeJson['joke']

print("Here is your joke: " + '"' + joke + '"')
