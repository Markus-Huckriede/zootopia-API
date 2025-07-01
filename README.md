<<<<<<< HEAD
# zootopia-API
=======
This project is a simple animal information website generator. It fetches animal data from an external API based on a user’s input and generates an HTML page displaying the animal’s details such as diet, location, and taxonomy. The main goal is to separate data fetching from website generation, allowing flexibility in data sources and cleaner code organization.

Problem it solves:
It provides an easy way to create informative animal webpages without manually gathering or formatting data.

Intended audience:
Developers learning API integration and web generation in Python, or anyone interested in building simple dynamic websites using external data.

Usage
Get your own API key:
Visit API Ninjas and sign up for a free account. After logging in, generate your API key for the Animals API.

Create a .env file:
In the root folder of the project, create a file named .env and add your API key like this:

ini
Code kopieren
API_KEY=your_api_key_here
Run the script:

nginx
Code kopieren
python animals_web_generator.py
Enter the name of an animal:
For example, type lion and press Enter.

View the results:
The script will generate an animals.html file with information about the animal you searched for.

Important Note
Your API key is private and should never be shared publicly or committed to version control. Each user must obtain their own API key from API Ninjas and store it securely in the .env file for the script to work properly.