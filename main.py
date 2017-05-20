from configuration.basic_configuration import BasicConfiguration
from utils.load_insult import load_insult
from admin.admin import admin

config_file = BasicConfiguration('./resources/configuration.ini')
admin = admin(config_file.admins)
insults = load_insult(config_file.insult_file)
taken_by = [False, None]


def main():
    from app import App
    app = App(config_file.token)
    app.run()


if __name__ == '__main__':
    main()
