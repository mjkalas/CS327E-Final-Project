import requests
import json


def post_some_dict(v, url):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    jsonString = str(requests.post(url, data=json.dumps(v), headers=headers))
    jsonObj = json.loads(jsonString)
    print(jsonObj.get("kind"))

values = {
  "request": {
    "passengers": {
      "adultCount": 1
    },
    "slice": [
      {
        "origin": "LAX",
        "destination": "NYC",
        "date": "2016-05-01"
      },
      {
        "origin": "NYC",
        "destination": "LAX",
        "date": "2016-05-07"
      }
    ],
    "solutions": "3"
  }
}

url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCaxLMRTwz6SrmthTns7-1wQT76Nw1k_qk'
post_some_dict(values, url)


