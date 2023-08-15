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

def add_new_country(country, num_of_visits, cities_visited):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = num_of_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


### TEST ###
# new_country = {}
# new_country["country"] = "Russia"
# new_country["visits"] = "2"
# new_country["cities"] = ["Moscow", "Saint Petersburg"]
# print(new_country)
# travel_log.append(new_country)
# print(travel_log[2])
