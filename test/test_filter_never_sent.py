from time import gmtime, sleep

import pytest

from src.filter_never_sent import FilterNeverSent
from src.page_filter import PageFilter
from src.page_reference import PageReference
from src.rss_configuration import RssConfiguration

feedparser_dict = [
    {
        'link': 'https://g1.globo.com/ce/ceara/noticia/2019/08/06/grupo-e-preso-com-arma-e-municao-apos-bater-carro-durante-perseguicao-na-grande-fortaleza.ghtml',
        'published_parsed': [2044, 8, 14, 3, 1, 3, 2, 226, 0]
    },
    {
        'link': 'https://g1.globo.com/loterias/noticia/2019/08/06/mega-sena-pode-pagar-r-32-milhoes-nesta-terca.ghtml',
        'published_parsed': [2018, 8, 14, 3, 1, 3, 2, 226, 0]
    },
    {
        'link': 'https://g1.globo.com/economia/noticia/2019/08/06/preco-medio-dos-imoveis-residenciais-ja-caiu-mais-de-2percent-em-2019-diz-fipezap.ghtml',
        'published_parsed': [2001, 8, 14, 3, 1, 3, 2, 226, 0]
    }
]


class TestFilterNeverSent:
    pages = [PageReference(i) for i in feedparser_dict]
    rss = 'http://g1.globo.com/dynamo/rss2.xml'

    @pytest.fixture(autouse=True)
    def before_any(self):
        c = RssConfiguration(self.rss).set_timestamp(list(gmtime()))

        del c
        self.config = RssConfiguration(self.rss)
        self.my_filter = FilterNeverSent(self.config)

    def test_init(self):
        assert type(self.my_filter._threshold) is list
        assert len(self.my_filter._threshold) == 9
        assert self.my_filter._config == self.config
        assert self.my_filter._last <= self.my_filter._threshold

    def test_inheritance(self):
        child_type = type(self.my_filter)
        assert issubclass(child_type, PageFilter)

    def test_threshold(self):
        sleep(1)
        assert list(gmtime()) > self.my_filter._threshold

    def test_filter_update_timestamp(self):
        assert len(self.pages) == 3
        timestamp = self.config.get_timestamp()
        pages = [self.my_filter.filter(p) for p in self.pages]
        assert pages == [True, False, False]
        assert timestamp < self.config._future_config[self.config._timestamp_field]

    def test_filter_no_update_timestamp(self):
        timestamp = self.config.get_timestamp()
        assert not self.my_filter.filter(self.pages[2])
        assert timestamp == self.config.get_timestamp()
