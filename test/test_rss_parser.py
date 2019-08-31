from src.page_reference import PageReference
from src.rss_parser import RssParser


class TestRssParser:
    rss = 'http://g1.globo.com/dynamo/rss2.xml'

    def test_get_links(self):
        parser = RssParser(TestRssParser.rss)
        pages = parser.get_pages()
        assert type(pages) is list
        assert len(pages) > 5
        assert type(pages[0]) is PageReference
        assert len(parser._rss.entries) == len(pages)

    def test_rss(self):
        rss = RssParser(TestRssParser.rss)._rss
        assert len(rss) > 5
        for entry in rss.entries:
            assert type(entry.link) is str
            assert len(entry.link) > 5
