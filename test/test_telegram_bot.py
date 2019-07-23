import pytest
from telegram_bot import TelegramBot


def test_send_msg():
    try:
        TelegramBot.send('Getting a little better')
        assert True
    except:
        assert False, "Could not send message"