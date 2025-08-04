import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}")
print(json.dumps(response.json(), indent = 2)) #it gives a json response, dumps gives a nice format

o = response.json()
for result in o["results"]:  
    print(result["trackName"])