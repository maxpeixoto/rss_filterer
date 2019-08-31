from src.page_reference import PageReference


class TestPageReference:
    feedparser_data = {'title': 'Mega-Sena pode pagar R$ 32 milhões nesta terça',
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
                                             'medium': 'image'}],
                       'tags': [{'term': 'G1', 'scheme': None, 'label': None}],
                       'published': 'Tue, 06 Aug 2019 03:01:02 -0000'}

    def test_init(self):
        page = PageReference(self.feedparser_data)
        assert type(page.link) is str

    def test_types_created(self):
        d = {"a": 1, "b": 2, "c": "xyz"}
        page = PageReference(d)
        assert page.a == 1
        assert page.b == 2
        assert page.c == "xyz"

    def test_add_type(self):
        d = {"a": 1, "b": 2, "c": "xyz"}
        page = PageReference(d)
        page.add("new_type", "new_val")
        assert page.new_type == "new_val"
