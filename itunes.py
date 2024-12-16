import json
import requests
import sys

if len(sys.argv)!=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])
'''print(json.dumps(response.json(), indent=3))'''

o = response.json()
for result in o["results"]:
    print(result["trackName"])