import json
import os


class Config(object):

    def __init__(self, file_name):
        self.file_name = file_name


def read_config(field):
    config_data = {}
    config_path = os.path.dirname(__file__)
    with open('{}/{}'.format(config_path, 'config_general.json')) as configFile:
        config_data = json.loads(configFile.read())
    return config_data[field]


def get_username():
    return read_config('username')


def get_password():
    return read_config('password')


def get_browser():
    return read_config('browser')


def get_report_path():
    return read_config('report_path')


# def get_browser():
#    browser = "lalala"
#   if browser == 'firefox':
#        print('')
#   elif browser == 0:
#      print('Zero')
# elif browser == 1:
#    print('Single')
# return browser


