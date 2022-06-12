travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

# TODO: Write the function that will allow new countries to be added to the travel_log.
def add_new_country(country_visited, cities_visited, total_visits):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = total_visits
    travel_log.append(new_country)

add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log)