from telegram.ext import Job
from commands import Command
from main import taken_by
from utils.get_info import get_info


@Command(pass_job_queue=True)
def take(bot, update, job_queue):
    taken_by_bool, taken_by_info = taken_by[0], taken_by[1]
    if taken_by_bool:
        info = get_info(taken_by_info)
        bot.sendMessage(chat_id=update.message.chat_id, text="The pass is taken by {0}.".format(info))
    else:
        job_queue.put(Job(callback=force_release, interval=10, repeat=False, context=update.message.chat_id))
        bot.sendMessage(chat_id=update.message.chat_id, text="The pass is our.")
        taken_by[0] = True
        taken_by[1] = update.message.to_dict()['from']


def force_release(bot, job):
    taken_by[0] = False
    bot.sendMessage(chat_id=job.context, text="The pass is release.")
