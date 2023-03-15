import requests
from bs4 import BeautifulSoup as bs4
from description import description as d


def scrap():
    url = "http://ovtok.com/lecl0i38j/home/ovtok/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs4(response.text, 'lxml')
        films = soup.select("div#hann")
        i = 0
        all = []
        for film in films:
            if i < 15:
                element = film.find('a')
                link = "http://ovtok.com"+element['href']
                all.append(d(link))
                i += 1
            else:
                return all
    else:
        print("Impossible de joindre le serveur")
        return None
