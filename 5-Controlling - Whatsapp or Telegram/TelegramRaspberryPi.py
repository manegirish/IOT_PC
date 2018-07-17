from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from telegram import Bot, Update


def chat_bot(bot: Bot, update: Update):
    print(update.message.text)
    try:
        bot.send_message(chat_id=update.message.chat_id, text=str(update.message.text).upper())
    except Exception as e:
        print(e)


def start(bot: Bot, update: Update):
    print(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text="I will not say hello world")


# Kick Start to bot.
def main():
    updater = Updater('568246727:AAEXYTCQECy5I-CFsXfy7KzSnQ2pKUdUvaY')
    updater.dispatcher.add_handler(MessageHandler(Filters.text, chat_bot))

    # Normal Start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
