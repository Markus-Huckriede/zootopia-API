import requests

with open("animals_template.html", "r") as file:
    template = file.read()

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">'
    output += f'<h2 class="card__title">{animal_obj["name"]}</h2>'
    output += '<div class="card__text">'
    output += f'Diet: {animal_obj["characteristics"]["diet"]}<br>'
    output += f'Location: {animal_obj["locations"][0]}<br>'
    output += f'Type: {animal_obj["taxonomy"]["class"]}'
    output += '</div>'
    output += '</li>'
    return output


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

def main():
    name = input("Enter a name of an animal: ")
    animals_data = fetch_animal_data(name)

    if not animals_data:
        animals_info = f" <h2>The animal '{name}' doesn't exist.</h2>"
    else:
        animals_info = ''
        for animal_obj in animals_data:
            animals_info += serialize_animal(animal_obj)

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w") as file:
        file.write(new_html)
        print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()
