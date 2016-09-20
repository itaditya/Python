import json
import requests

j = json.loads(requests.get(
    "http://quotes.stormconsultancy.co.uk/random.json").text)
print j["author"], j["quote"]
