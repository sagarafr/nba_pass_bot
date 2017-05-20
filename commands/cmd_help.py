from commands import Command


@Command()
def help(bot, update):
    help_message = "*start: Tell something.\n" \
                   "*take: Take the token.\n" \
                   "*status: Tell who have take the token.\n" \
                   "*release: Release the token.\n" \
                   "*add_insult: Add an insult in the parameter (admin only).\n" \
                   "*insult: Tell an insult only if the token is taken.\n"
    bot.sendMessage(chat_id=update.message.chat_id, text=help_message)
