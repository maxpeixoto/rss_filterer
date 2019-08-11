from telegram_bot import TelegramBot


def test_send_msg():
    try:
        TelegramBot.send('Getting a little better')
    except:
        assert False, "Could not send message"


def test_send_empty_msg():
    try:
        TelegramBot.send('')
    except:
        assert False, "Could not send message"
