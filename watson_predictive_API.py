import json 

with open("fake-json-data.json", "r") as json_file:
    data = json.load(json_file)

print(data["response"][0]["pageName"])