from telegram.ext import Updater, CommandHandler
import logging

URL=open('proxy.txt').read().split('\n')[0]
login=open('proxy.txt').read().split('\n')[1]
credetionals=open('proxy.txt').read().split('\n')[2]
tmetoken=open('tmetoken.txt').read().split('\n')[0]

PROXY ={'proxy_url': URL,
    'urllib3_proxy_kwargs':{'username':login,'password':credetionals}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    greet_text='Вызван /start'
    logging.info(greet_text)
    update.message.reply_text(greet_text)

def main():
    tmebot = Updater(tmetoken, request_kwargs=PROXY)

    logging.info('Бот запускается') 

    dp=tmebot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    tmebot.start_polling()
    tmebot.idle()


main()
