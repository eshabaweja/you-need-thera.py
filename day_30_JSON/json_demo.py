'''JavaScript Object Notation'''
import json

with open("states.json") as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['area_codes'])
    del state['abbreviation']

with open("new_states.json","w") as ns:
    json.dump(data, ns, indent=2)
