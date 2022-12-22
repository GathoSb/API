import requests 

class ApiConnection():
    def __init__(self,pokemon_name):
        self.url=f'https://pokeapi.co/api/v2/pokemon/ditto{pokemon_name}'
        
    def makeRequests(self):
        response = requests.get(self.url)
        print(response)
        print(response.status_code)
        json_response = response.json()
        for item in json_response ['stats']:
            print(f'el stats {item["stat"]["nombre"]} tiene un valor de {item["base_stat"]}')


api_connection = ApiConnection('Mewtow')
api_connection.makeRequests()
print(api_connection)
