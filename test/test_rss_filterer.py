import pytest

from src.rss_filterer import RssFilterer


class TestRssFilterer:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.rss = 'http://g1.globo.com/dynamo/rss2.xml'
        self.filterer = RssFilterer(self.rss)

    def test_init(self):
        assert self.filterer._rss == self.rss

    def test_filter(self):
        pages = self.filterer.filter()._pages
        assert type(pages) is list
