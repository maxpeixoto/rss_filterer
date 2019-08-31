from src.page_filterer import PageFilterer
from src.rss_parser import RssParser
from src.telegram_bot import TelegramBot


class TestMain:
    rss = 'http://g1.globo.com/dynamo/rss2.xml'

    def test_full(self):
        pages = RssParser(TestMain.rss).get_pages()
        total = len(pages)
        pages = PageFilterer(TestMain.rss).filter_pages_parallel(pages)
        assert 0 < len(pages) < total
        TelegramBot.send("Encontrados %d links" % len(pages))
