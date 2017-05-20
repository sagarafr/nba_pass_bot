from commands import Command


@Command()
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="The man bear pork is online.")
