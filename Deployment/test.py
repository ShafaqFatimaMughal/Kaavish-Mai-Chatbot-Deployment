import requests

URL = "https://predicttest1-i2x734b46q-el.a.run.app/"
while True:
    data = input("Text:")
    print(requests.get(URL+"greeting").text)