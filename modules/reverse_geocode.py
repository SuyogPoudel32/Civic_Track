
import requests
def reverse_geocode(latitude, longitude):
    url = "https://nominatim.openstreetmap.org/reverse"

    params = {
        "lat": latitude,
        "lon": longitude,
        "format": "json"
    }

    headers = {
        "User-Agent": "CivicIssueReportingSystem/1.0"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("display_name", "Unknown Location")

    return "Unknown Location"