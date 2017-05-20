from commands import Command
from main import taken_by


@Command(pass_job_queue=True)
def release(bot, update, job_queue):
    taken_by_bool, taken_by_info = taken_by[0], taken_by[1]
    user = update.message.to_dict()['from']
    if taken_by_bool:
        if user == taken_by_info:
            taken_by[0] = False
            for job in job_queue.jobs():
                if job.name == 'force_release':
                    job.schedule_removal()
            bot.sendMessage(chat_id=update.message.chat_id, text="The pass is release.")
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text="Your are not the right user.")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="The pass is release.")
