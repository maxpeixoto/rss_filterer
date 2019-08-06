import feedparser

from link import Link


class RssParser:
    def __init__(self, rss):
        self._rss = feedparser.parse(rss)

    def get_links(self):
        return [Link(i) for i in self._rss.entries]
