travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_country(t_log, country, visits, cities):
    t_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })

add_country(travel_log, "poconos", 5, ["inna","minna","deeka"])

print(travel_log)