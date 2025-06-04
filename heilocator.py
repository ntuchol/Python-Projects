pip install geopy
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="hei_locator")
    location = geolocator.geocode("desired location")
    if location:
        latitude = location.latitude
        longitude = location.longitude
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Location not found.")
        
        

    from geopy.geocoders import Nominatim

    geolocator = Nominatim(user_agent = "hei_locator")

    location = geolocator.geocode("Eiffel Tower")

    if location:
      print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    else:
      print("Location not found")