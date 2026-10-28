import ctypes
import subprocess
import urllib.request

import requests

try:
    response = requests.get("https://science.nasa.gov/wp-json/wp/v2/apod-basic")
    data = response.json()
    if data["media_type"] == "image":
        try:
            subprocess.run(
                ["del", "apod.jpg"],
                cwd="C:/Users/CWPERR8189/Documents/python",
                check=True,
            )
        except FileNotFoundError:
            print("> No previous image found to delete.")

        url = data["hdurl"]
        urllib.request.urlretrieve(url, "apod.jpg")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\CWPERR8189\Documents\python\apod.jpg", 0x01 | 0x02)

    else:
        print("> Media not a still image.")
        print("> Background not changed.")

except requests.exceptions.HTTPError as err:
    print(f"HTTPError: {err}")
