import requests

API_KEY = '0K1fwHLpvK0kCtztNfwR7Q==xpgs5EGeVJ76ua69'

def fetch_animal_data(name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': '0K1fwHLpvK0kCtztNfwR7Q==xpgs5EGeVJ76ua69'})
    if response.status_code == requests.codes.ok:
        data = response.json()
        if data:
            return data
        else:
            print(f"The animal {name} doesn't exist")
            return None
    else:
        print("Error:", response.status_code, response.text)
        return None
