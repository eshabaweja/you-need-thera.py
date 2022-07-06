import json

people_string = '''
{
    "people" : [
        {
            "name":"Jane Doe",
            "phone": "7989652122",
            "emails":["jandoe@gmail.com","janet69@gmail.com"],
            "has_license": true
        },{
            "name":"John Smith",
            "phone": "6589969696",
            "emails":["jonnyboi@gmail.com","jsmith@gmail.com"],
            "has_license": false
        }
    ]
}
'''
# load a json string into a python object using loads()
people_data = json.loads(people_string)
# print(type(people_data["people"][0]["name"]))
for person in people_data["people"]:
    print(person,"\n")


# dump a python object into a json string using dumps()
for person in people_data["people"]:
    # delete key AND value
    del person["phone"]
# use the indent argument to make it readable
new_data = json.dumps(people_data, indent=2)
print(new_data)