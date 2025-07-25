import googlemaps

API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
gmaps = googlemaps.Client(key=API_KEY)

origin = "34th Street, New York, NY"
destination = "42nd Street, New York, NY"

directions_result = gmaps.directions(origin, destination, mode="walking")

if directions_result:
    steps = directions_result[0]['legs'][0]['steps']
    print("Directions:")
    for step in steps:
        print(step['html_instructions'].replace('<b>', '').replace('</b>', '').replace('<div style="font-size:0.9em">', ' ').replace('</div>', ''))
else:
    print("No directions found.")
