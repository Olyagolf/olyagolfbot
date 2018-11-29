from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
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

def talk_to_me(bot, update):
    user_text="Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    tmebot = Updater(tmetoken, request_kwargs=PROXY)

    logging.info('Бот запускается') 

    dp=tmebot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    tmebot.start_polling()
    tmebot.idle()


main()
