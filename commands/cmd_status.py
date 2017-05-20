from commands import Command
from main import taken_by
from utils.get_info import get_info


@Command()
def status(bot, update):
    taken_by_bool, taken_by_info = taken_by[0], taken_by[1]
    if taken_by_bool:
        info = get_info(taken_by_info)
        bot.sendMessage(chat_id=update.message.chat_id, text="The pass is taken by {0}.".format(info))
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="The pass is release.")
