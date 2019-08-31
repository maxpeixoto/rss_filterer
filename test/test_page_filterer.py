import pytest

from src.page_filter import PageFilter
from src.page_filterer import PageFilterer
from src.page_reference import PageReference


class TestPageFilterer:

    @pytest.fixture(autouse=True)
    def before_all(self):
        feedparser_dict = [
            {
                'link': 'https://g1.globo.com/ce/ceara/noticia/2019/08/06/grupo-e-preso-com-arma-e-municao-apos-bater-carro-durante-perseguicao-na-grande-fortaleza.ghtml',
                'published_parsed': [2044, 8, 14, 3, 1, 3, 2, 226, 0],
                'summary': 'grupo e preso com arma e municao apos bater carro durante perseguicao na grande fortaleza'
            },
            {
                'link': 'https://g1.globo.com/loterias/noticia/2019/08/06/mega-sena-pode-pagar-r-32-milhoes-nesta-terca.ghtml',
                'published_parsed': [2022, 8, 14, 3, 1, 3, 2, 226, 0],
                'summary': 'mega sena pode pagar r 32 milhoes nesta terca'
            },
            {
                'link': 'https://g1.globo.com/economia/noticia/2019/08/06/preco-medio-dos-imoveis-residenciais-ja-caiu-mais-de-2percent-em-2019-diz-fipezap.ghtml',
                'published_parsed': [2001, 8, 14, 3, 1, 3, 2, 226, 0],
                'summary': 'preco medio dos imoveis residenciais ja caiu mais de 2percent em 2019 diz fipezap'
            }
        ]

        self.pages = [PageReference(i) for i in feedparser_dict]

        self.rss = 'http://g1.globo.com/dynamo/rss2.xml'
        self.filterer = PageFilterer(self.rss)

    def test_init(self):
        assert type(self.filterer) is PageFilterer
        assert self.filterer._rss == self.rss

    def test_filter_list(self):
        assert type(self.filterer._filters) is list
        assert len(self.filterer._filters) > 0
        for f in self.filterer._filters:
            assert isinstance(f, PageFilter)

    def test_filter_page_parallel(self):
        assert len(self.pages) == 3
        pages = self.filterer.filter_pages_parallel(self.pages)
        assert len(pages) == 2
        links = [page.link for page in pages]
        assert 'https://g1.globo.com/economia/noticia/2019/08/06/preco-medio-dos-imoveis-residenciais-ja-caiu-mais-de-2percent-em-2019-diz-fipezap.ghtml' not in links
