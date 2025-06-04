def city_search(city_name, city_list):
  """
  Checks if a city exists in a list of cities.

  Args:
    city_name: The name of the city to search for (string).
    city_list: A list of city names (strings).

  Returns:
    True if the city is found in the list, False otherwise.
  """
  for city in city_list:
    if city.lower() == city_name.lower():
      return True
  return False

# Example usage:
cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]

# Search for a city that exists in the list
search_city = "london"
if city_search(search_city, cities):
  print(f"{search_city} found in the list.")
else:
  print(f"{search_city} not found in the list.")

# Search for a city that does not exist in the list
search_city = "Berlin"
if city_search(search_city, cities):
  print(f"{search_city} found in the list.")
else:
  print(f"{search_city} not found in the list.")