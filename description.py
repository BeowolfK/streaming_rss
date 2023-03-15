import requests
from bs4 import BeautifulSoup as bs4
from re import split, findall


def description(link):
    desc = requests.get(link)
    if desc.status_code == 200:
        content = bs4(desc.text, 'lxml')
        div = content.select("html body div div div center b i")[0]
        image = content.select("html body div div div p img")[0]["src"]
        regex = split("\s\([0-9]{4}\)\s", div.text.strip(), 1)
        title = regex[0]
        year = findall("(\s*[0-9]{4}\s*)", div.text.strip(), 0)[0]
        desc = content.select(" html body div div div p")[2].text.strip()
        return [title, image, year, desc, link]
    else:
        return None
