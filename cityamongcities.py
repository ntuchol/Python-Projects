def city_search(city_name, city_list):
  
  for city in city_list:
    if city.lower() == city_name.lower():
      return True
  return False

cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]

search_city = "london"
if city_search(search_city, cities):
  print(f"{search_city} found in the list.")
else:
  print(f"{search_city} not found in the list.")

search_city = "Berlin"
if city_search(search_city, cities):
  print(f"{search_city} found in the list.")
else:
  print(f"{search_city} not found in the list.")
