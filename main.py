import logging

from rss_filterer import RssFilterer
from rss_list import RssList
from telegram_bot import TelegramBot

if __name__ == "__main__":
    try:
        while True:
            for rss in RssList.get():
                TelegramBot.send('links vindos de ' + rss)
                logging.debug("rss: %s" % rss)
                RssFilterer(rss).filter().send_links()
    except Exception as e:
        TelegramBot.send('Erro fatal. Parei de mandar links por causa disso: %s' % str(e))
        """"
        Known issues:
        Busca nao pega non ASC characters
        Busca em propagandas, nao so no texto principal
        Nao da pra instalar
        Apenas mostra links como resultado
        nao loga em arquivo
        """
