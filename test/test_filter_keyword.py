import pytest

from src.filter_keyword import FilterKeyword
from src.page_reference import PageReference


class TestFilterKeyword:
    feedparser_dict = {
        'title': 'Grupo é preso com arma e munição após bater carro durante perseguição na Grande Fortaleza',
        'title_detail': {'type': 'text/plain', 'language': None,
                         'base': 'https://g1.globo.com/rss/g1/',
                         'value': 'Grupo é preso com arma e munição após bater carro durante perseguição na Grande Fortaleza'},
        'links': [{'rel': 'alternate', 'type': 'text/html',
                   'href': 'https://g1.globo.com/ce/ceara/noticia/2019/08/06/grupo-e-preso-com-arma-e-municao-apos-bater-carro-durante-perseguicao-na-grande-fortaleza.ghtml'}],
        'link': 'https://g1.globo.com/ce/ceara/noticia/2019/08/06/grupo-e-preso-com-arma-e-municao-apos-bater-carro-durante-perseguicao-na-grande-fortaleza.ghtml',
        'id': 'https://g1.globo.com/ce/ceara/noticia/2019/08/06/grupo-e-preso-com-arma-e-municao-apos-bater-carro-durante-perseguicao-na-grande-fortaleza.ghtml',
        'guidislink': False,
        'summary': '<img src="https://s2.glbimg.com/Sa_5gZQwHm4C0WaSykMbS9opp2Y=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/D/e/Sj6EmTTTAX6nr7BI1OVw/whatsapp-image-2019-08-05-at-22.48.05.jpeg" /><br />   Todos os integrantes do grupo têm antecedentes criminais. Criminosos colidiram o carro com um poste ao tentar fugir da polícia durante uma perseguição em Maracanaú.\nRafaela Duarte/ Sistema Verdes Mares\nQuatro homens foram presos após colidirem o carro em um poste durante uma perseguição policial em Maracanaú, Região Metropolitana de Fortaleza, na noite desta segunda-feira (5). Os agentes apreenderam com os suspeitos uma arma calibre 38, munição, uma pistola falsa e um aparelho que bloqueia o sinal de alarmes de veículos. \nDe acordo com a polícia, a perseguição teve início no Novo Maracanaú, após policiais do 14º Batalhão receberem informações que criminosos estavam realizando assaltos na região.\n No cruzamento da Avenida Parque Sul com Avenida Parque Leste, no Distrito Industrial I, o carro que os suspeitos estavam perdeu o controle. Após o acidente, um dos criminosos saiu do veículo e tentou fugir correndo, mas foi capturado. O carro usado na ação estava com as placas clonadas e foi levado para a delegacia.\nConforme levantamento dos policiais, todos os integrantes do grupo têm antecedentes criminais. Os homens foram identificados como Geyrlison Alves do Amaral , 27, com antecedentes por tráfico e receptação; Antônio Marcos Silva Maciel , 20, com antecedentes por homicídio, assalto, roubo de veículo, lesão corporal e dano ao patrimônio; Jorge Luis Cardoso Mariano, 22, com antecedente por assalto; e Claudemir de Sousa Batista , 20, que responde criminalmente por um homicídio.\nSegundo a polícia, a quadrilha é da região da Comunidade Babilônia, em Fortaleza. Após a prisão, o grupo foi encaminhado para a Delegacia Metropolitana de Maracanaú.\nAgentes apreenderam com os suspeitos uma arma calibre 38, munição, uma pistola falsa e um bloqueador universal.\nRafaela Duarte/ Sistema Verdes Mares',
        'summary_detail': {'type': 'text/html', 'language': None,
                           'base': 'https://g1.globo.com/rss/g1/',
                           'value': '<img src="https://s2.glbimg.com/Sa_5gZQwHm4C0WaSykMbS9opp2Y=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/D/e/Sj6EmTTTAX6nr7BI1OVw/whatsapp-image-2019-08-05-at-22.48.05.jpeg" /><br />   Todos os integrantes do grupo têm antecedentes criminais. Criminosos colidiram o carro com um poste ao tentar fugir da polícia durante uma perseguição em Maracanaú.\nRafaela Duarte/ Sistema Verdes Mares\nQuatro homens foram presos após colidirem o carro em um poste durante uma perseguição policial em Maracanaú, Região Metropolitana de Fortaleza, na noite desta segunda-feira (5). Os agentes apreenderam com os suspeitos uma arma calibre 38, munição, uma pistola falsa e um aparelho que bloqueia o sinal de alarmes de veículos. \nDe acordo com a polícia, a perseguição teve início no Novo Maracanaú, após policiais do 14º Batalhão receberem informações que criminosos estavam realizando assaltos na região.\n No cruzamento da Avenida Parque Sul com Avenida Parque Leste, no Distrito Industrial I, o carro que os suspeitos estavam perdeu o controle. Após o acidente, um dos criminosos saiu do veículo e tentou fugir correndo, mas foi capturado. O carro usado na ação estava com as placas clonadas e foi levado para a delegacia.\nConforme levantamento dos policiais, todos os integrantes do grupo têm antecedentes criminais. Os homens foram identificados como Geyrlison Alves do Amaral , 27, com antecedentes por tráfico e receptação; Antônio Marcos Silva Maciel , 20, com antecedentes por homicídio, assalto, roubo de veículo, lesão corporal e dano ao patrimônio; Jorge Luis Cardoso Mariano, 22, com antecedente por assalto; e Claudemir de Sousa Batista , 20, que responde criminalmente por um homicídio.\nSegundo a polícia, a quadrilha é da região da Comunidade Babilônia, em Fortaleza. Após a prisão, o grupo foi encaminhado para a Delegacia Metropolitana de Maracanaú.\nAgentes apreenderam com os suspeitos uma arma calibre 38, munição, uma pistola falsa e um bloqueador universal.\nRafaela Duarte/ Sistema Verdes Mares'},
        'media_content': [{
            'url': 'https://s2.glbimg.com/Sa_5gZQwHm4C0WaSykMbS9opp2Y=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/D/e/Sj6EmTTTAX6nr7BI1OVw/whatsapp-image-2019-08-05-at-22.48.05.jpeg',
            'medium': 'image'}], 'tags': [{'term': 'G1', 'scheme': None, 'label': None}],
        'published': 'Tue, 06 Aug 2019 03:55:42 -0000'
    }
    page = PageReference(feedparser_dict)

    @pytest.fixture(autouse=True)
    def before_all(self):
        self.filter = FilterKeyword()

    def test_init(self):
        assert type(self.filter._keywords) is list

    def test_get_page_content(self):
        page = self.filter._get_page_content("http://www.google.com")
        assert type(page) is str
        assert len(page) is not 0

    def test_has_keyword(self):
        match = self.filter._has_keyword("http://instantrimshot.com/")
        assert match == "Instant rimsho"

    def test_no_keyword(self):
        match = self.filter._has_keyword("http://pudim.com.br")
        assert match is False

    def test_add_keyword(self):
        try:
            self.page.keyword
            assert False
        except AttributeError:
            assert True
        match = self.filter.filter(self.page)
        assert match == "No cruzamento da Avenida Parque Sul com Avenida Parque Leste"
        assert self.page.keyword == "No cruzamento da Avenida Parque Sul com Avenida Parque Leste"
