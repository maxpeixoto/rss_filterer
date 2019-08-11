import urllib.request

from keyword_reader import KeywordReader
from link_filter import LinkFilter


class FilterKeyword(LinkFilter):
    def __init__(self):
        self._keywords = KeywordReader.read()

    def _get_page_content(self, link):
        return str(urllib.request.urlopen(link, timeout=12).read())

    def _has_keyword(self, link):
        content = self._get_page_content(link)
        return any(word in content for word in self._keywords)

    def filter(self, page):
        return self._has_keyword(page.link)
