import requests 

url = "https://pythonjobs.github.io/"
resp = requests.get(url)

print(resp.text)