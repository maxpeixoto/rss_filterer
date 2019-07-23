from keyword_reader import KeywordReader
from link_filterer import LinkFilterer
from rss_reader import RssReader
from rss_parser import RssParser
from telegram_bot import TelegramBot
from rss_time import RssTime

links = [
    'https://g1.globo.com/sp/ribeirao-preto-franca/noticia/2019/07/20/moradores-reivindicam-circulacao-de-onibus-urbano-em-bairro-de-jardinopolis-sp.ghtml',
    'https://g1.globo.com/es/espirito-santo/noticia/2019/07/20/crianca-liga-carro-invade-calcada-e-quebra-vidraca-de-loja-no-centro-de-linhares-no-es.ghtml',
    'https://g1.globo.com/to/tocantins/noticia/2019/07/20/adolescente-de-14-anos-e-apreendida-suspeita-de-tentar-matar-homem-a-facadas.ghtml',
    'https://g1.globo.com/mg/triangulo-mineiro/noticia/2019/07/20/crianca-e-transferida-para-rede-particular-apos-acidente-na-br-365-em-uberlandia-em-que-motorista-tentou-desviar-de-lobo-guara.ghtml',
    'https://g1.globo.com/ro/rondonia/noticia/2019/07/20/quase-400-beneficiarios-do-orgulho-do-madeira-devem-assinar-os-contratos-em-ro.ghtml',
    #'https://g1.globo.com/al/alagoas/noticia/2019/07/20/recuperacao-de-pavimento-interdita-trecho-da-av-gustavo-paiva-em-cruz-das-almas.ghtml',
    #'https://g1.globo.com/rj/norte-fluminense/noticia/2019/07/20/eja-vai-abrir-4-mil-vagas-para-ensino-fundamental-para-o-segundo-semestre-em-campos-no-rj.ghtml',
    #'https://g1.globo.com/rj/rio-de-janeiro/noticia/2019/07/20/familia-schurmann-faz-nova-expedicao-por-rio-e-sao-paulo-no-combate-ao-lixo-plastico-no-mar.ghtml',
    #'https://g1.globo.com/sp/santos-regiao/edicao/2019/07/20/videos-jornal-da-tribuna-1-edicao-de-sabado-20-de-julho.ghtml',
    #'https://g1.globo.com/sp/piracicaba-regiao/noticia/2019/07/20/buracos-na-avenida-1o-de-agosto-afetam-transito-e-representam-riscos-aos-condutores-em-piracicaba.ghtml',
    #'https://g1.globo.com/mg/minas-gerais/o-que-fazer-em-belo-horizonte/noticia/2019/07/20/moraes-moreira-garante-sucessos-na-virada-cultural-de-bh-e-diz-nao-vou-decepcionar-meu-publico.ghtml',
    #'https://g1.globo.com/sp/sorocaba-jundiai/noticia/2019/07/20/tim-afirma-que-apagao-na-regiao-de-sorocaba-foi-causada-por-falha-em-equipamento-central.ghtml',
    #'https://g1.globo.com/ba/bahia/noticia/2019/07/20/fenomeno-swell-ondas-gigantes-e-ventos-fortes-atraem-surfistas-baianos-para-litoral-de-salvador.ghtml',
    #'https://g1.globo.com/mt/mato-grosso/noticia/2019/07/20/mae-e-filho-sao-presos-em-mt-por-estelionato-ao-aplicarem-golpe-em-venda-de-carro.ghtml',
    #'https://g1.globo.com/sp/mogi-das-cruzes-suzano/noticia/2019/07/20/policia-militar-recupera-em-suzano-carro-roubado-em-2016-em-sao-paulo.ghtml',
    #'https://g1.globo.com/sp/ribeirao-preto-franca/noticia/2019/07/20/ribeirao-preto-registra-45-mortes-no-transito-no-primeiro-semestre-aponta-infosiga.ghtml',
    #'https://g1.globo.com/ms/mato-grosso-do-sul/noticia/2019/07/20/jovem-baleado-pelo-pai-em-ms-durante-discussao-o-denuncia-a-policia-por-violacao-de-domicilio.ghtml',
    #'https://g1.globo.com/pr/norte-noroeste/noticia/2019/07/20/pm-e-receita-federal-descobrem-barracao-com-cigarros-contrabandeados-em-londrina.ghtml',
    #'https://g1.globo.com/pi/piaui/noticia/2019/07/20/tres-pessoas-sao-encontradas-mortas-dentro-de-chacara-no-sul-do-piaui.ghtml',
    #'https://g1.globo.com/pe/petrolina-regiao/noticia/2019/07/20/vigilancia-sanitaria-lanca-sistema-online-em-petrolina-pe.ghtml',
    #'https://g1.globo.com/sp/sao-paulo/noticia/2019/07/20/policial-aposentado-e-baleado-no-ipiranga-na-zona-sul-de-sp.ghtml',
    #'https://g1.globo.com/sp/sao-jose-do-rio-preto-aracatuba/noticia/2019/07/20/justica-decreta-prisao-preventiva-de-irmaos-que-balearam-guarda-municipal-em-assalto-a-padaria.ghtml',
    #'https://g1.globo.com/go/goias/noticia/2019/07/20/pais-denunciam-que-recem-nascida-sofreu-queimaduras-em-incubadora-de-hospital-de-goiania.ghtml',
    #'https://g1.globo.com/sp/sao-carlos-regiao/noticia/2019/07/20/1a-feira-ceramica-decor-de-porto-ferreira-reune-150-lojas-com-descontos-de-ate-50percent.ghtml',
    #'https://g1.globo.com/rj/sul-do-rio-costa-verde/noticia/2019/07/20/denuncias-anonimas-ajudam-a-prender-homens-que-enterravam-drogas-em-barra-mansa.ghtml',
    #'https://g1.globo.com/sp/piracicaba-regiao/noticia/2019/07/20/operacao-contra-trafico-e-exploracao-sexual-lacra-oito-bares-por-falta-de-alvara-em-capivari.ghtml',
    #'https://g1.globo.com/ac/cruzeiro-do-sul-regiao/noticia/2019/07/20/mais-de-30-mil-pessoas-sao-esperadas-para-a-5a-edicao-do-festival-da-banana-em-rodrigues-alves-ac.ghtml',
    #'https://g1.globo.com/pe/petrolina-regiao/edicao/2019/07/20/videos-gr1-de-sabado-20-de-julho.ghtml',
    #'https://g1.globo.com/ce/ceara/edicao/2019/07/20/videos-cetv-1-edicao-de-sabado-20-de-julho.ghtml',
    #'https://g1.globo.com/pa/santarem-regiao/edicao/2019/07/20/videos-jornal-tapajos-1-edicao-de-sabado-20-de-julho.ghtml',
    #'https://g1.globo.com/pb/paraiba/edicao/2019/07/20/videos-jpb1-deste-sabado-20-de-julho.ghtml',
    #'https://g1.globo.com/sp/santos-regiao/noticia/2019/07/20/baixada-santista-registra-queda-de-4percent-no-numero-de-acidentes-fatais-1o-semestre-de-2019-diz-infosiga.ghtml',
    #'https://g1.globo.com/ac/acre/noticia/2019/07/20/crm-ac-abre-sindicancia-para-apurar-conduta-de-medico-preso-em-operacao-da-policia-civil.ghtml',
    #'https://g1.globo.com/sp/campinas-regiao/noticia/2019/07/20/orquestra-sinfonica-arte-viva-recebe-toquinho-em-concerto-gratuito-em-campinas.ghtml',
    #'https://g1.globo.com/ce/ceara/noticia/2019/07/20/onca-amarrada-em-arvore-por-moradores-salta-e-tenta-fugir-ao-ser-resgatada-em-reriutaba-no-ceara-veja-video.ghtml',
    #'https://g1.globo.com/sp/sao-paulo/noticia/2019/07/20/sptrans-reorganiza-17-itinerarios-de-linhas-de-onibus-na-zona-sul-de-sp.ghtml',
    #'https://g1.globo.com/ms/mato-grosso-do-sul/edicao/2019/07/20/videos-mstv-1-edicao-de-campo-grande-sabado-20-de-julho.ghtml',
    #'https://g1.globo.com/ap/amapa/noticia/2019/07/20/policia-prende-caseiro-e-apreende-adolescente-suspeitos-de-matarem-tecnico-em-enfermagem.ghtml',
    #'https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2019/07/20/dois-homens-sao-presos-por-roubo-e-trafico-de-drogas-em-taubate.ghtml',
    'https://g1.globo.com/am/amazonas/edicao/2019/07/20/videos-jam-1-edicao-deste-sabado-20-de-julho-de-2019.ghtml'
]

if __name__ == "__main__":
    RssTime.get_time() #TODO continuar daqui
    #TelegramBot.send('Testando um dois 3')
    links = RssParser.get_links(RssReader.read())

    print(links)
    print("total de links: %s" % len(links))

    keywords = KeywordReader.read()
    filterer = LinkFilterer(keywords)
    links = filterer.filter_links_parallel(links)

    print(links)
    print("total de links: %s" % len(links))
    [TelegramBot.send(link) for link in links]

    """"
    Known issues:
    Busca nao pega non ASC characters
    Busca em propagandas, nao so no texto principal
    Nao da pra instalar
    Apenas mostra links como resultado
    """
