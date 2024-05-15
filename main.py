import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.leagueoflegends.com/es-mx/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

all_links = []

# Buscar todas las etiquetas 'a'
results = soup.find_all('a')

for a in results:
    #comprobar si la etiqueta 'a' tiene el atributo 'href'
    if 'href' in a.attrs:
        all_links.append(a['href'])

data = {}

for link in all_links:
    try:
        #Obtiene el contenido de la página
        response = requests.get(link)
        page_soup = BeautifulSoup(response.content, 'html.parser')

        #Busca las etiquetas 'h1' y 'p'
        all_h1 = [tag.text for tag in page_soup.find_all('h1')]
        all_p = [tag.text for tag in page_soup.find_all('p')]

        #Almacena los resultados en el diccionario data
        data[link] = {
            'h1': all_h1,
            'p': all_p
        }

        #Imprimir los links, h1 y todos los p encontrados
        print(f"Link: {link}")
        print(f"h1 tags: {all_h1}")
        print(f"p tags: {all_p}")
        print("\n")
    except:
        #Si hay un error almacenar un array vacío
        data[link] = {
            'h1': [],
            'p': []
        }

#guardar los resultados en un archivo JSON
with open('data.json', 'w') as f:
    json.dump(data, f)
