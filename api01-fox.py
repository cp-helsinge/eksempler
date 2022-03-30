import requests

download = requests.get("http://randomfox.ca/floof")

print(download.status_code)

#200 = ok
#404 = ikke fundet - har du selv fundet på den url?

print(download.json())
