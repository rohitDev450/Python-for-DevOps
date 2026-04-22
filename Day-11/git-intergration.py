import requests

url = f"https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)
if response.status_code == 200:
    pulls = response.json()
    
for pull in pulls:
    print(pull["user"]["login"])