from configparser import ConfigParser


class BasicConfiguration(object):
    def __init__(self, file):
        self._parser = ConfigParser()
        with open(file, 'r') as fd_file:
            self._parser.read_file(fd_file)
            self._admin = None if not self._parser.has_option('DEFAULT', 'admins') else [int(e) for e in self._parser['DEFAULT']['admins'].split(';')]

    @property
    def token(self):
        return None if not self._parser.has_option('DEFAULT', 'token') else str(self._parser['DEFAULT']['token'])

    @property
    def admins(self):
        return self._admin
