from commands import Command
from main import insults
from main import taken_by
from random import randint


@Command()
def insult(bot, update):
    taken_by_bool, taken_by_info = taken_by[0], taken_by[1]
    if taken_by_bool:
        bot.sendMessage(chat_id=update.message.chat_id, text="{0}".format(insults[randint(0, len(insults) - 1)]))
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="You can't insult without reason")
