import pytest
from rss_parser import RssParser

def test_rss_is_list():
    rss = 'http://g1.globo.com/dynamo/rss2.xml'
    parser = RssParser(rss)
    assert type(parser._rss) is list
    assert len(parser._rss) > 5
    assert type(parser._rss[0]) is str
    assert len(parser._rss[0]) > 5

def test_links_is_list():
    rss = 'http://g1.globo.com/dynamo/rss2.xml'
    parser = RssParser(rss)
    links = parser.get_links()
    assert type(links) is list
