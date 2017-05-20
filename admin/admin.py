from functools import wraps


def admin(user_group):

    def group_restriction(func):

        @wraps(func)
        def wrapper(bot, update, *args, **kwargs):
            # extract user_id from arbitrary update
            try:
                user_id = update.message.from_user.id
            except (NameError, AttributeError):
                try:
                    user_id = update.inline_query.from_user.id
                except (NameError, AttributeError):
                    try:
                        user_id = update.chosen_inline_result.from_user.id
                    except (NameError, AttributeError):
                        try:
                            user_id = update.callback_query.from_user.id
                        except (NameError, AttributeError):
                            print("No user_id available in update.")
                            return
            if user_id not in user_group:
                print(user_id, user_group, user_id in user_group)
                print("Unauthorized access denied : ", user_id)
                return
            return func(bot, update, *args, **kwargs)
        return wrapper
    return group_restriction
