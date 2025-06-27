import googlemaps

# Initialize the Google Maps client with your API key
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
gmaps = googlemaps.Client(key=API_KEY)

# Define the origin and destination
origin = "34th Street, New York, NY"
destination = "42nd Street, New York, NY"

# Request directions
directions_result = gmaps.directions(origin, destination, mode="walking")

# Parse and display the directions
if directions_result:
    steps = directions_result[0]['legs'][0]['steps']
    print("Directions:")
    for step in steps:
        print(step['html_instructions'].replace('<b>', '').replace('</b>', '').replace('<div style="font-size:0.9em">', ' ').replace('</div>', ''))
else:
    print("No directions found.")