import requests

base_url = "http://httpbin.org"

# resp = requests.get(base_url + "/get")
# print(resp.status_code)
# # print(resp.content)
# resp = resp.json()
# print(resp['headers'])
# print(resp['headers']['Host'])
# print(resp['headers']['User-Agent'])

payload = {'username':'student', 'password':'telacad'}
resp = requests.post(base_url + "/post", json=payload)
print(resp.status_code)
print(resp.json())