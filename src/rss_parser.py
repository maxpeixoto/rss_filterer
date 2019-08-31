import feedparser

from src.page_reference import PageReference


class RssParser:
    def __init__(self, rss):
        self._rss = feedparser.parse(rss)

    def get_pages(self):
        return [PageReference(i) for i in self._rss.entries]
