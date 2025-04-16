import requests
import folium

def get_location_details(place):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={place}"
    response = requests.get(url, headers={"User-Agent": "EchoMap+ App"})
    data = response.json()
    if data:
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])
        name = data[0]['display_name']
        return lat, lon, name
    else:
        return None, None, None

def create_map(lat, lon, name):
    map_obj = folium.Map(location=[lat, lon], zoom_start=14)
    folium.Marker([lat, lon], tooltip=name, popup=name).add_to(map_obj)
    return map_obj

