"parcer top 50 actors"
import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import jsonlines

URL_TEMPLATE = "https://www.imdb.com/search/name/?gender=male%2Cfemale&ref_=nv_cel_m"
URL_start = 'https://www.imdb.com'
r = requests.get(URL_TEMPLATE)

result_list = []
soup = bs(r.text, "html.parser")
actors_names = soup.find_all('h3', class_='lister-item-header')
bio_actors = soup.find_all('p', class_ = None)
for name, bio in zip(actors_names, bio_actors):
    r_born = requests.get(URL_start + name.find('a').get('href')+'/')
    soup_born = bs(r_born.text, "html.parser")
    res_born = soup_born.find('script', type="application/ld+json")
    json_object = json.loads(res_born.contents[0])
    
    r_film = requests.get(URL_start + name.find('a').get('href')+'/')
    soup_film = bs(r_film.text, "html.parser")
    res_film = soup_film.find('div', id ="filmography").find_all('a', href = True, class_ = None, limit = 15)
    
    result_list.append({'bio':  bio.get_text().strip(), 
                        'born': pd.to_datetime(json_object['birthDate']).strftime('%Y-%-m-%-d').strip(),
                        'movies': [res_film[i].get_text() for i in range(len(res_film))], 
                        'movie_links': [(URL_start + res_film[i].get('href')) for i in range(len(res_film))],
                        'name': name.a.string.rstrip().strip(), 
                        'url':  URL_start + name.find('a').get('href')+'/'})
    
with jsonlines.open('output.jsonl', 'w') as writer:
    writer.write_all(result_list)
