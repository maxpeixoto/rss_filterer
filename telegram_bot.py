import logging
from urllib import request

from page_reference import PageReference


class TelegramBot:
    TOKEN = ""
    CHAT_ID = ""
    @staticmethod
    def send(msg):
        if type(msg) is PageReference:
            real_msg = ' '.join([msg.keyword, msg.link, msg.keyword])
            return TelegramBot.send(real_msg)
        try:
            if msg:
                url = "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s" % (
                    TelegramBot.TOKEN, TelegramBot.CHAT_ID, msg)
                request.urlopen(url)
        except Exception as e:
            logging.error("Nao foi possivel enviar msg via Telegram. msg:%s. Erro:%s" % (msg, str(e)))
