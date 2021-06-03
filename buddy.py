import json
json_string = """{
    "name": "John Sutton",
    "age": 31,
    "city": "New York"
    }
"""

json_object = json.loads(json_string)
print(json_object['name'])