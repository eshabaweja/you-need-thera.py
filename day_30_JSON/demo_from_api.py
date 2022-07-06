import json
from urllib.request import urlopen

with urlopen("https://zenquotes.io/api/quotes") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data,indent=2))
for item in data:
    print(f"q: {item['q']}\na: {item['a']}\n")