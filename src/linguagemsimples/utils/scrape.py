from requests import get
from rest_framework.exceptions import ParseError, NotFound
from bs4 import BeautifulSoup
from typing import List, Dict
from django.utils.translation import gettext_lazy as _


class Scrape(object):

    def get_webpage_videos(self, ID_SESSION: int) -> str:
        URL = 'https://www.camara.leg.br/evento-legislativo/{}'
        page = get(URL.format(ID_SESSION), verify=False)
        return page

    def scraping_videos(self, page: str) -> List:
        soup = BeautifulSoup(page, 'html.parser')

        videos = soup.find_all(class_='chamada__link-trecho linkReproduzir')

        json_video = [self.format_videos(video) for video in videos]

        return json_video

    def format_videos(self, video) -> Dict:
        try:
            description = video.get_text().strip()
            description = description.split("\n")
            response = {'url': video['url'],
                        'author': description[0],
                        'legend': description[2],
                        'schedule': description[4][:-1],
                        'duration': description[5],
                        'thumbnail': video.find('img')['src']}
        except IndexError:
            response = {'error': 'Error get description'}
        except AttributeError:
            response = {'error': 'Error get description'}

        return response

    def get_file_video(self, url: str) -> str:
        if 'https://www.camara.leg.br/evento-legislativo' in url:
            page = get(url, verify=False)
            return page
        else:
            raise NotFound(detail=_('Invalid url information'), code=404)

    def scraping_file_video(self, page: str) -> List:
        soup = BeautifulSoup(page, 'html.parser')

        video = soup.find('source')

        try:
            url_file = video['src']
        except TypeError:
            raise ParseError(detail=_('Error parser file video'), code=400)

        return url_file
