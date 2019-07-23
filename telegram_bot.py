from urllib import request


class TelegramBot:
    TOKEN = ""
    CHAT_ID = ""

    @staticmethod
    def send(msg):
        url = "https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s" % (
        TelegramBot.TOKEN, TelegramBot.CHAT_ID, msg)
        request.urlopen(url)
