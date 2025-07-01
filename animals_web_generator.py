import data_fetcher


with open("animals_template.html", "r") as file:
    template = file.read()


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
    name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_animal_data(name)


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
