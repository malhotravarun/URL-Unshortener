import sys
import requests

try:
    link = sys.argv[1]
    response = requests.get(link)
    print(response.url)
except requests.exceptions.MissingSchema:
    print("Syntax error!!")
    print("Example -> python redirect https://bit.ly/abc")
