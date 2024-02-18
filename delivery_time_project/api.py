import requests

# Replace with your MapmyIndia API key
MAPPLE_API_KEY = 'b4afc8042f8dcb557a29c9bff6eb47ec'

# Origin and destination addresses (replace with your values)
origin = "wakad"
destination = "pimpri"

# Construct the API URL with parameters
url = f"https://apis.mapmyindia.com/routing/v1/driving?origin={origin}&destination={destination}&apiKey={MAPPLE_API_KEY}"

# Make the API request
response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()

        # Extract duration from response in minutes
        duration_minutes = data['route']['duration'] // 60

        print("Estimated travel time:", duration_minutes, "minutes")

        # Access other route information as needed, e.g.,
        # distance = data['route']['distance']  # in meters
        # steps = data['route']['steps']  # list of route steps

    except Exception as e:
        print("Error processing API response:", e)
else:
    print("API request failed:", response.status_code, response.text)
