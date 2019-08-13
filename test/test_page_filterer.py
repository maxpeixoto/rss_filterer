import pytest

from page_filter import PageFilter
from page_filterer import PageFilterer
from page_reference import PageReference


class TestPageFilterer:

    @pytest.fixture(autouse=True)
    def before_all(self):
        feedparser_dict = [
            {'title': 'Grupo é preso com arma e munição após bater carro durante perseguição na Grande Fortaleza',
             'title_detail': {'type': 'text/plain', 'language': None, 'base': 'https://g1.globo.com/rss/g1/',
                              'value': 'Grupo é preso com arma e munição após bater carro durante perseguição na Grande Fortaleza'},
             'links': [{'rel': 'alternate', 'type': 'text/html',
                        'href': 'https://g1.globo.com/ce/ceara/noticia/2019/08/06/grupo-e-preso-com-arma-e-municao-apos-bater-carro-durante-perseguicao-na-grande-fortaleza.ghtml'}],
             'link': 'https://g1.globo.com/ce/ceara/noticia/2019/08/06/grupo-e-preso-com-arma-e-municao-apos-bater-carro-durante-perseguicao-na-grande-fortaleza.ghtml',
             'id': 'https://g1.globo.com/ce/ceara/noticia/2019/08/06/grupo-e-preso-com-arma-e-municao-apos-bater-carro-durante-perseguicao-na-grande-fortaleza.ghtml',
             'guidislink': False,
             'summary': '<img src="https://s2.glbimg.com/Sa_5gZQwHm4C0WaSykMbS9opp2Y=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/D/e/Sj6EmTTTAX6nr7BI1OVw/whatsapp-image-2019-08-05-at-22.48.05.jpeg" /><br />   Todos os integrantes do grupo têm antecedentes criminais. Criminosos colidiram o carro com um poste ao tentar fugir da polícia durante uma perseguição em Maracanaú.\nRafaela Duarte/ Sistema Verdes Mares\nQuatro homens foram presos após colidirem o carro em um poste durante uma perseguição policial em Maracanaú, Região Metropolitana de Fortaleza, na noite desta segunda-feira (5). Os agentes apreenderam com os suspeitos uma arma calibre 38, munição, uma pistola falsa e um aparelho que bloqueia o sinal de alarmes de veículos. \nDe acordo com a polícia, a perseguição teve início no Novo Maracanaú, após policiais do 14º Batalhão receberem informações que criminosos estavam realizando assaltos na região.\n No cruzamento da Avenida Parque Sul com Avenida Parque Leste, no Distrito Industrial I, o carro que os suspeitos estavam perdeu o controle. Após o acidente, um dos criminosos saiu do veículo e tentou fugir correndo, mas foi capturado. O carro usado na ação estava com as placas clonadas e foi levado para a delegacia.\nConforme levantamento dos policiais, todos os integrantes do grupo têm antecedentes criminais. Os homens foram identificados como Geyrlison Alves do Amaral , 27, com antecedentes por tráfico e receptação; Antônio Marcos Silva Maciel , 20, com antecedentes por homicídio, assalto, roubo de veículo, lesão corporal e dano ao patrimônio; Jorge Luis Cardoso Mariano, 22, com antecedente por assalto; e Claudemir de Sousa Batista , 20, que responde criminalmente por um homicídio.\nSegundo a polícia, a quadrilha é da região da Comunidade Babilônia, em Fortaleza. Após a prisão, o grupo foi encaminhado para a Delegacia Metropolitana de Maracanaú.\nAgentes apreenderam com os suspeitos uma arma calibre 38, munição, uma pistola falsa e um bloqueador universal.\nRafaela Duarte/ Sistema Verdes Mares',
             'summary_detail': {'type': 'text/html', 'language': None, 'base': 'https://g1.globo.com/rss/g1/',
                                'value': '<img src="https://s2.glbimg.com/Sa_5gZQwHm4C0WaSykMbS9opp2Y=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/D/e/Sj6EmTTTAX6nr7BI1OVw/whatsapp-image-2019-08-05-at-22.48.05.jpeg" /><br />   Todos os integrantes do grupo têm antecedentes criminais. Criminosos colidiram o carro com um poste ao tentar fugir da polícia durante uma perseguição em Maracanaú.\nRafaela Duarte/ Sistema Verdes Mares\nQuatro homens foram presos após colidirem o carro em um poste durante uma perseguição policial em Maracanaú, Região Metropolitana de Fortaleza, na noite desta segunda-feira (5). Os agentes apreenderam com os suspeitos uma arma calibre 38, munição, uma pistola falsa e um aparelho que bloqueia o sinal de alarmes de veículos. \nDe acordo com a polícia, a perseguição teve início no Novo Maracanaú, após policiais do 14º Batalhão receberem informações que criminosos estavam realizando assaltos na região.\n No cruzamento da Avenida Parque Sul com Avenida Parque Leste, no Distrito Industrial I, o carro que os suspeitos estavam perdeu o controle. Após o acidente, um dos criminosos saiu do veículo e tentou fugir correndo, mas foi capturado. O carro usado na ação estava com as placas clonadas e foi levado para a delegacia.\nConforme levantamento dos policiais, todos os integrantes do grupo têm antecedentes criminais. Os homens foram identificados como Geyrlison Alves do Amaral , 27, com antecedentes por tráfico e receptação; Antônio Marcos Silva Maciel , 20, com antecedentes por homicídio, assalto, roubo de veículo, lesão corporal e dano ao patrimônio; Jorge Luis Cardoso Mariano, 22, com antecedente por assalto; e Claudemir de Sousa Batista , 20, que responde criminalmente por um homicídio.\nSegundo a polícia, a quadrilha é da região da Comunidade Babilônia, em Fortaleza. Após a prisão, o grupo foi encaminhado para a Delegacia Metropolitana de Maracanaú.\nAgentes apreenderam com os suspeitos uma arma calibre 38, munição, uma pistola falsa e um bloqueador universal.\nRafaela Duarte/ Sistema Verdes Mares'},
             'media_content': [{
                                   'url': 'https://s2.glbimg.com/Sa_5gZQwHm4C0WaSykMbS9opp2Y=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/D/e/Sj6EmTTTAX6nr7BI1OVw/whatsapp-image-2019-08-05-at-22.48.05.jpeg',
                                   'medium': 'image'}], 'tags': [{'term': 'G1', 'scheme': None, 'label': None}],
             'published': 'Tue, 06 Aug 2019 03:55:42 -0000'},

            {'title': 'Mega-Sena pode pagar R$ 32 milhões nesta terça',
             'title_detail': {'type': 'text/plain', 'language': None, 'base': 'https://g1.globo.com/rss/g1/',
                              'value': 'Mega-Sena pode pagar R$ 32 milhões nesta terça'}, 'links': [
                {'rel': 'alternate', 'type': 'text/html',
                 'href': 'https://g1.globo.com/loterias/noticia/2019/08/06/mega-sena-pode-pagar-r-32-milhoes-nesta-terca.ghtml'}],
             'link': 'https://g1.globo.com/loterias/noticia/2019/08/06/mega-sena-pode-pagar-r-32-milhoes-nesta-terca.ghtml',
             'id': 'https://g1.globo.com/loterias/noticia/2019/08/06/mega-sena-pode-pagar-r-32-milhoes-nesta-terca.ghtml',
             'guidislink': False,
             'summary': '<img src="https://s2.glbimg.com/JC6Olrj3y5Bw8noSiAj8fabOVT0=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/H/i/BjMFSLTd68zGX2TBtUag/volantes-loterias-q98a7776-credito-marcelo-brandt-g1.jpg" /><br />   Apostas podem ser feitas até as 19h, em lotéricas ou pela internet. Concurso 2.175 pode pagar R$ 32 milhões\nMarcelo Brandt/G1\nO concurso 2.176 pode pagar um prêmio de R$ 32 milhões para quem acertar as seis dezenas. O sorteio ocorre às 20h (horário de Brasília) desta terça-feira (6) em São Paulo (SP).\nPara apostar na Mega-Sena\nAs apostas podem ser feitas até as 19h (de Brasília) do dia do sorteio, em qualquer lotérica do país ou pela internet. A aposta mínima custa R$ 3,50.\nProbabilidades\nA probabilidade de vencer em cada concurso varia de acordo com o número de dezenas jogadas e do tipo de aposta realizada. Para a aposta simples, com apenas seis dezenas, com preço de R$ 3,50, a probabilidade de ganhar o prêmio milionário é de 1 em 50.063.860, segundo a Caixa.\nJá para uma aposta com 15 dezenas (limite máximo), com o preço de R$ 17.517,50, a probabilidade de acertar o prêmio é de 1 em 10.003, ainda segundo a Caixa.\nSabe como é calculado o prêmio? Veja no vídeo abaixo:\nSaiba como é calculado o prêmio da Mega-Sena',
             'summary_detail': {'type': 'text/html', 'language': None, 'base': 'https://g1.globo.com/rss/g1/',
                                'value': '<img src="https://s2.glbimg.com/JC6Olrj3y5Bw8noSiAj8fabOVT0=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/H/i/BjMFSLTd68zGX2TBtUag/volantes-loterias-q98a7776-credito-marcelo-brandt-g1.jpg" /><br />   Apostas podem ser feitas até as 19h, em lotéricas ou pela internet. Concurso 2.175 pode pagar R$ 32 milhões\nMarcelo Brandt/G1\nO concurso 2.176 pode pagar um prêmio de R$ 32 milhões para quem acertar as seis dezenas. O sorteio ocorre às 20h (horário de Brasília) desta terça-feira (6) em São Paulo (SP).\nPara apostar na Mega-Sena\nAs apostas podem ser feitas até as 19h (de Brasília) do dia do sorteio, em qualquer lotérica do país ou pela internet. A aposta mínima custa R$ 3,50.\nProbabilidades\nA probabilidade de vencer em cada concurso varia de acordo com o número de dezenas jogadas e do tipo de aposta realizada. Para a aposta simples, com apenas seis dezenas, com preço de R$ 3,50, a probabilidade de ganhar o prêmio milionário é de 1 em 50.063.860, segundo a Caixa.\nJá para uma aposta com 15 dezenas (limite máximo), com o preço de R$ 17.517,50, a probabilidade de acertar o prêmio é de 1 em 10.003, ainda segundo a Caixa.\nSabe como é calculado o prêmio? Veja no vídeo abaixo:\nSaiba como é calculado o prêmio da Mega-Sena'},
             'media_content': [{
                                   'url': 'https://s2.glbimg.com/JC6Olrj3y5Bw8noSiAj8fabOVT0=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/H/i/BjMFSLTd68zGX2TBtUag/volantes-loterias-q98a7776-credito-marcelo-brandt-g1.jpg',
                                   'medium': 'image'}], 'tags': [{'term': 'G1', 'scheme': None, 'label': None}],
             'published': 'Tue, 06 Aug 2019 03:01:02 -0000'},

            {'title': 'Preço médio dos imóveis residenciais já caiu mais de 2% em 2019, diz FipeZap',
             'title_detail': {'type': 'text/plain', 'language': None, 'base': 'https://g1.globo.com/rss/g1/',
                              'value': 'Preço médio dos imóveis residenciais já caiu mais de 2% em 2019, diz FipeZap'},
             'links': [{'rel': 'alternate', 'type': 'text/html',
                        'href': 'https://g1.globo.com/economia/noticia/2019/08/06/preco-medio-dos-imoveis-residenciais-ja-caiu-mais-de-2percent-em-2019-diz-fipezap.ghtml'}],
             'link': 'https://g1.globo.com/economia/noticia/2019/08/06/preco-medio-dos-imoveis-residenciais-ja-caiu-mais-de-2percent-em-2019-diz-fipezap.ghtml',
             'id': 'https://g1.globo.com/economia/noticia/2019/08/06/preco-medio-dos-imoveis-residenciais-ja-caiu-mais-de-2percent-em-2019-diz-fipezap.ghtml',
             'guidislink': False,
             'summary': '<img src="https://s2.glbimg.com/p0pCS_nXRujAg9WX-ZdMhWMNhd4=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/B/N/zzYvVNT2uPtMRbcvcfbA/img-3033.jpg" /><br />   O número leva em conta a comparação entre a alta de 0,26% dos preços no acumulado do ano e a inflação de 2,46% esperada para o mesmo período.  O preço médio dos imóveis residenciais acumulou até julho deste ano uma queda de 2,15%, segundo pesquisa FipeZap divulgada nesta terça-feira (5). O número leva em conta a comparação entre a alta de 0,26% dos preços no acumulado do ano e a inflação de 2,46% esperada para o mesmo período. \nA pesquisa leva em conta o valor dos anúncios de imóveis à venda. Para fazer a comparação com a inflação, o estudo considera a previsão do boletim Focus, do Banco Central, para o Índice de Preços ao Consumidor Amplo (IPCA) – considerado o índice de inflação oficial do país. \nDependente de recursos do FGTS, setor da construção enfrenta recuperação lenta\nNa passagem de junho para julho, os preços dos imóveis tiveram queda de 0,03% - o que, levando em conta a inflação de 0,23% esperada para o mês, significa uma queda real de 0,26%. \nNos últimos 12 meses, a alta acumulada é de 0,28% - que significa queda real de 2,89% se for levada em conta a inflação de 3,26% esperada para o período. \nValor médio de venda dos imóveis comerciais caiu nos primeiros sete meses de 2019, diz pesquisa\nGlauco Araújo/G1',
             'summary_detail': {'type': 'text/html', 'language': None, 'base': 'https://g1.globo.com/rss/g1/',
                                'value': '<img src="https://s2.glbimg.com/p0pCS_nXRujAg9WX-ZdMhWMNhd4=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/B/N/zzYvVNT2uPtMRbcvcfbA/img-3033.jpg" /><br />   O número leva em conta a comparação entre a alta de 0,26% dos preços no acumulado do ano e a inflação de 2,46% esperada para o mesmo período.  O preço médio dos imóveis residenciais acumulou até julho deste ano uma queda de 2,15%, segundo pesquisa FipeZap divulgada nesta terça-feira (5). O número leva em conta a comparação entre a alta de 0,26% dos preços no acumulado do ano e a inflação de 2,46% esperada para o mesmo período. \nA pesquisa leva em conta o valor dos anúncios de imóveis à venda. Para fazer a comparação com a inflação, o estudo considera a previsão do boletim Focus, do Banco Central, para o Índice de Preços ao Consumidor Amplo (IPCA) – considerado o índice de inflação oficial do país. \nDependente de recursos do FGTS, setor da construção enfrenta recuperação lenta\nNa passagem de junho para julho, os preços dos imóveis tiveram queda de 0,03% - o que, levando em conta a inflação de 0,23% esperada para o mês, significa uma queda real de 0,26%. \nNos últimos 12 meses, a alta acumulada é de 0,28% - que significa queda real de 2,89% se for levada em conta a inflação de 3,26% esperada para o período. \nValor médio de venda dos imóveis comerciais caiu nos primeiros sete meses de 2019, diz pesquisa\nGlauco Araújo/G1'},
             'media_content': [{
                                   'url': 'https://s2.glbimg.com/p0pCS_nXRujAg9WX-ZdMhWMNhd4=/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/B/N/zzYvVNT2uPtMRbcvcfbA/img-3033.jpg',
                                   'medium': 'image'}], 'tags': [{'term': 'G1', 'scheme': None, 'label': None}],
             'published': 'Tue, 06 Aug 2019 03:00:02 -0000'}]

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
        assert 'https://g1.globo.com/economia/noticia/2019/08/06/preco-medio-dos-imoveis-residenciais-ja-caiu-mais-de-2percent-em-2019-diz-fipezap.ghtml' in links
