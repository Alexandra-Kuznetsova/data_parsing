import requests
from bs4 import BeautifulSoup as bs
import json
import jsonlines

%%time
URL_TEMPLATE = "https://www.imdb.com/search/name/?gender=male%2Cfemale&ref_=nv_cel_m"
URL_start = 'https://www.imdb.com'
r = requests.get(URL_TEMPLATE)

result_list = []
soup = bs(r.text, "html.parser")
actors_names = soup.find_all('h3', class_='lister-item-header')
for name in actors_names:
    
    r_film = requests.get(URL_start + name.find('a').get('href')+'/')
    soup_film = bs(r_film.text, "html.parser")
    res_film = soup_film.find('div', id ="filmography").find_all('a', href = True, class_ = None, limit = 15)
    
    for i in range(len(res_film)):
        r_actors = requests.get(URL_start + res_film[i].get('href'))
        soup = bs(r_actors.text, "html.parser")
        res = soup.find_all('div',attrs={"data-testid":"title-cast-item"})
        result_list.append({'movie_links': (URL_start + res_film[i].get('href')),
                            'title': res_film[i].get_text().strip(),  
                            'cast': [i.find('a').get('aria-label').strip() for i in res], 
                            'url': [URL_start + i.find('a').get('href') for i in res]})

with jsonlines.open('output.jsonl', 'w') as writer:
    writer.write_all(result_list)
