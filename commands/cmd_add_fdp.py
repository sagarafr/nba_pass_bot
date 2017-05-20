from commands import Command
from main import insults
from main import config_file
from main import admin


@Command(pass_args=True)
@admin
def add_insult(bot, update, args):
    args = ' '.join(args) + '\n'
    try:
        insults.index(args)
    except ValueError:
        insults.append(args)
        with open(config_file.insult_file, 'a') as fd:
            fd.write(args)
        bot.sendMessage(chat_id=update.message.chat_id, text="The insult is register.")
