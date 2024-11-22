import requests
import os
from config import Config


class Gbooks():
    def __init__(self, results_per_page=5):
        self.start_page_index = 0
        self.results_per_page = results_per_page

    def search(self, query):
        titles = []
        authors = []

        params = {'q': query, 'startIndex': self.start_page_index,
                  'key': Config.GOOGLE_API_KEY}

        response = requests.get(
            url='https://www.googleapis.com/books/v1/volumes', params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            total_items = data.get('totalItems', 0)
            for entry in data['items']:
                try:
                    titles.append(entry['volumeInfo']['title'])
                except:
                    pass
                try:
                    authors.append(entry['volumeInfo']['author'])
                except:
                    pass
            return titles, authors, total_items
        else:
            return 'Error fetching data'

    def next_page(self):
        self.start_page_index += self.results_per_page

    def previous_page(self):
        if self.start_page_index >= self.results_per_page:
            self.start_page_index -= self.results_per_page
