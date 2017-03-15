from html.parser import HTMLParser
from urllib.request import urlopen

WIKIPEDIA_URL = 'https://en.wikipedia.org/wiki/List_of_programming_languages'


class ProgLangParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside_interesting_part = False
        self.inside_li_tag = False
        self.current_data = ''
        self.programming_languages = []

    def parse(self):
        self.feed(self._getHTML())
        return self.programming_languages

    def handle_starttag(self, tag, attrs):
        id_tags = [val for (attr, val) in attrs if attr == 'id']

        if 'A' in id_tags:
            self.inside_interesting_part = True
        elif 'See_also' in id_tags:
            self.inside_interesting_part = False

        if self.inside_interesting_part and tag == 'li':
            self.inside_li_tag = True

    def handle_endtag(self, tag):
        if self.inside_interesting_part and tag == 'li':
            self.inside_li_tag = False
            self.programming_languages.append(self.current_data)
            self.current_data = ''

    def handle_data(self, data):
        if self.inside_li_tag:
            self.current_data = self.current_data + data

    def _getHTML(self):
        response = urlopen(WIKIPEDIA_URL)
        data = response.read()
        return data.decode('utf-8')
