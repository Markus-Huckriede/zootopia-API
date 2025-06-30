import json

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

def main():
    animals_data = load_data("animals_data.json")

    animals_info = ''
    for animal_obj in animals_data:
        animals_info += serialize_animal(animal_obj)

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w") as file:
        file.write(new_html)

if __name__ == "__main__":
    main()
