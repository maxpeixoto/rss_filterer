import logging

from page_filterer import PageFilterer
from rss_parser import RssParser
from telegram_bot import TelegramBot


class RssFilterer:
    def __init__(self, rss):
        self._rss = rss
        self._pages = None

    def filter(self):
        pages = RssParser(self._rss).get_pages()
        logging.info("total de links: %d" % len(pages))
        self._pages = PageFilterer(self._rss).filter_pages_parallel(pages)
        logging.info("total de links apos filtros: %d" % len(pages))
        return self

    def send_links(self):
        if len(self._pages):
            [TelegramBot.send(page.link) for page in self._pages]
