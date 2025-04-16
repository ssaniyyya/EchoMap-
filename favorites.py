import json
import os

FILENAME = "favorites.json"

def get_favorites():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_favorite(location_name):
    favorites = get_favorites()
    if location_name not in favorites:
        favorites.append(location_name)
        with open(FILENAME, "w") as f:
            json.dump(favorites, f)


