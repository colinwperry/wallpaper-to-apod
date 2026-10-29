import ctypes
import subprocess
import urllib.request

import requests

try:
    response = requests.get("https://science.nasa.gov/wp-json/wp/v2/apod-basic")
    data = response.json()
    
    if data["media_type"] == "image":
        if "hdurl" in data:
            url = data["hdurl"]
            urllib.request.urlretrieve(url, "apod.jpg")

            ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:/apod_wallpaper/apod", 0x01 | 0x02)
        
        else:
            raise FileNotFoundError("hdurl key does not exist in var data")
        
    else:
        print("> Media not a still image.")
        print("> Background not changed.")

except requests.exceptions.HTTPError as err:
    print(f"> HTTPError: {err}")
except FileNotFoundError as err:
    print(f"> FileNotFoundError: {err}")
else:
    print("> Wallpaper successfully changed")
