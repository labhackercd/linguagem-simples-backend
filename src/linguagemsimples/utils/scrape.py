from requests import get
from bs4 import BeautifulSoup
from typing import Dict


DictResponse = Dict[str, str]


class Scrape(object):

    def get_webpage_videos(self, ID_SESSION: int) -> str:
        URL = 'https://www.camara.leg.br/evento-legislativo/{}'
        page = get(URL.format(ID_SESSION))
        return page

    def scraping_videos(self, page: str) -> DictResponse:
        soup = BeautifulSoup(page, 'html.parser')

        videos = soup.find_all(class_='chamada__link-trecho linkReproduzir')

        json_video = dict()
        for count, video in enumerate(videos, start=1):
            json_video[count] = {'url': video['url'],
                                 'description': video.get_text().strip(),
                                 'thumbnail': video.find('img')['src']}

        return json_video
