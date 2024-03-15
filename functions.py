import shutil
import re
from geopy.geocoders import Nominatim


def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and its contents have been successfully deleted.")
    except FileNotFoundError:
        print(f"Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def is_valid_email(email):
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(email_regex, email))

def get_location(longitude, latitude):
    geolocator = Nominatim(user_agent="ch7al-machya")
    location = geolocator.reverse((latitude, longitude))
    return location.address