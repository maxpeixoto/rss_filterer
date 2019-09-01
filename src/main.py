import logging

from src.rss_filterer import RssFilterer
from src.rss_list import RssList
from src.telegram_bot import TelegramBot

if __name__ == "__main__":
    try:
        while True:
            for rss in RssList.get():
                logging.debug("rss: %s" % rss)
                RssFilterer(rss).filter().send_links()
    except Exception as e:
        TelegramBot.send('Erro fatal. Parei de mandar links por causa disso: %s' % str(e))
        """"
        Known issues:
        Busca nao pega non ASC characters
        nao loga em arquivo
        """
