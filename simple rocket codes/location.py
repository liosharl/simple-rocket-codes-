import time

def retrieve_rocket_location():
    # Simulate retrieving the rocket's location from a database or ground station
    # Replace this with actual data retrieval logic
    return (100, 200, 300)  # Example: Latitude, Longitude, Altitude in meters

while True:
    latitude, longitude, altitude = retrieve_rocket_location()
    print(f"Rocket Location: Latitude={latitude}, Longitude={longitude}, Altitude={altitude} meters")
    
    # Wait for 3 seconds before the next location update
    time.sleep(3)  # Sleep for 3 seconds
