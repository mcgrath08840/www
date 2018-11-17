import requests
from json import JSONDecodeError

#

r = requests.post('http://text-processing.com/api/sentiment', data={'text': 'hello world'})
try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("We could not decode the JSON response!")
except KeyError:
    print("We got json back but no key label.")

