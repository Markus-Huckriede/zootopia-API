import requests

name = input("Enter animal's name: ")
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': '0K1fwHLpvK0kCtztNfwR7Q==xpgs5EGeVJ76ua69'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
