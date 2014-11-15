import requests, random

html = requests.get("http://xkcd.com/%d" % random.randint(1,1446)).text
print(html)
