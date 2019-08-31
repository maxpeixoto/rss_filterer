import urllib.request

from keyword_reader import KeywordReader
from page_filter import PageFilter


class FilterKeyword(PageFilter):
    def __init__(self):
        self._keywords = KeywordReader.read()

    def _get_page_content(self, link):
        return str(urllib.request.urlopen(link, timeout=12).read())

    def _has_keyword(self, link):
        content = self._get_page_content(link)
        for word in self._keywords:
            if word in content:
                return word
        return False

    def filter(self, page):
        keyword = self._has_keyword(page.link)
        page.add('keyword', keyword)
        return keyword
