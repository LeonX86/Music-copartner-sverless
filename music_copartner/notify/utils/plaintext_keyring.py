# coding=utf-8
"""
Plaintext keyring module
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import os
import stat
import configparser

class PlaintextKeyring(object):
    def __init__(self, filename = None):
        if filename is None:
            filename = os.path.expanduser('~')
            filename = os.path.join(filename, '.plaintext_keyring')
        self.filename = filename
        # Create required directory
        if not os.path.exists(os.path.dirname(self.filename)):
            os.makedirs(os.path.dirname(self.filename))

    def get_password(self, service_name, username):
        config = configparser.SafeConfigParser()
        config.read([self.filename])
        try:
            return config.get(service_name, username)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return ""

    def set_password(self, service_name, username, password):
        config = configparser.SafeConfigParser()
        config.read([self.filename])
        if not config.has_section(service_name):
            config.add_section(service_name)
        config.set(service_name, username, password)
        fo = open(self.filename, 'wb')
        config.write(fo)
        fo.close()
        # change permission of the file
        os.chmod(self.filename, stat.S_IRUSR | stat.S_IWUSR)

    def delete_password(self, service_name, username):
        config = configparser.SafeConfigParser()
        config.read([self.filename])
        config.set(service_name, username, "")
        fo = open(self.filename, 'wb')
        config.write(fo)
        fo.close()
        # change permission of the file
        os.chmod(self.filename, stat.S_IRUSR | stat.S_IWUSR)
