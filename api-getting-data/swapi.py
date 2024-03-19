import requests
import json
import random

r = requests.get('https://swapi.dev/api/planets/' + str(random.randint(0, 50))).text
data = json.loads(r)
print(data)
out = json.dumps(data, indent=4)
with open("planets.json", "w") as f:
	    f.write(out)