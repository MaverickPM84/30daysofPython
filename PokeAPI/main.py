#How to connect to an API using Python

import requests

#base url variable to store the main API url so that it is easy to handle later on

base_url = "https://pokeapi.co/api/v2/"

#name parameter is used to get pokemon info

def get_pokemon_info(name):

    url = f"{base_url}/pokemon/{name}"
    # use requests module to capture the response. output of the requests module is response object - <Response [200]> , 200 HTTP response code means that it is OK

    response = requests.get(url)

    #capture response and how appropriate messages

    if response.status_code == 200:

        pokemon_data = response.json()   #use .json method to convert it to a dictionary
        return pokemon_data

    else:
        print(f"Failed to retrieve data {response.status_code}")



#pokemon name 
pokemon_name = 'bulbasaur'

pokemon_info = get_pokemon_info(pokemon_name)   #argument and parameter can be named different

# if pokemon info dictionary exists/True then print the info

if pokemon_info:
    print(f" Name: {pokemon_info["name"].capitalize()}")
    print(f" Id: {pokemon_info["id"]}")
    print(f" Height: {pokemon_info["height"]}")
    print(f" Weight: {pokemon_info["weight"]}")
    
