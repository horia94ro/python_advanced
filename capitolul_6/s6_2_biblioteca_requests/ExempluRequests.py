import requests

resp = requests.get("https://telacad.ro")
print(resp.status_code)
print(resp.content)
print(dir(resp))