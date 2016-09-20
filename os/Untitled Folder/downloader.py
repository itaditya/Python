import requests
import json

print("...")
f = open("a.json", 'r')
d = f.read()
for i in range(15):
    data = json.loads(d)[i]["_id"]
    response = requests.delete(
        'http://45.55.228.207:52295/schoolclass/' + data)
f.close()
