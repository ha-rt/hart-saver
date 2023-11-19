from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def returnLinks(link):
    response = get(link)
    bs = BeautifulSoup(response.text, 'html.parser')
    base_url = response.url

    links = []

    for a in bs.find_all('a', href=True):
        href = a["href"]
        absolute_url = urljoin(base_url, href)

        links.append(absolute_url)

    return links