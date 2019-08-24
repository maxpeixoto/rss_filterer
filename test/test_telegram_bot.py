from telegram_bot import TelegramBot


def test_send_msg():
    TelegramBot.send('Getting a little better')


def test_send_empty_msg():
    TelegramBot.send('')
