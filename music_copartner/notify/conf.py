# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import os
import configparser
from io import StringIO

DEFAULT_CONFIG="""
[smtp]
host = localhost
port = 25

[mail]
from_addr = notify@localhost
to_addr =
subject = Notify: %(prog)s has %(status)s
encoding = None

[auth]
username =
"""

def get_user_config_filename(appname='notify'):
    """
    Get user config filename.

    It will return operating system dependent config filename.

    Parameters
    ----------
    appname : string
        An application name used for filename

    Returns
    -------
    string
        A filename of user configuration.

    """
    import platform
    system = platform.system()
    if system == 'Windows':
        rootname = os.path.join(os.environ['APPDATA'], appname)
        filename = appname + ".cfg"
        prefix = ''
    elif system == 'Linux':
        XDG_CONFIG_HOME = os.environ.get('XDG_CONFIG_HOME', None)
        rootname = XDG_CONFIG_HOME or os.path.join('~', '.config')
        rootname = os.path.expanduser(rootname)
        # check if XDG_CONFIG_HOME exists
        if not os.path.exists(rootname) and XDG_CONFIG_HOME is None:
            # XDG_CONFIG_HOME is not used
            rootname = os.path.expanduser('~')
            filename = appname + ".cfg"
            prefix = '.'
        else:
            rootname = os.path.join(rootname, appname)
            filename = appname + ".cfg"
            prefix = ''
    elif system == 'Darwin':
        rootname = os.path.expanduser('~')
        filename = appname + ".cfg"
        prefix = '.'
    else:
        # Unknown
        rootname = os.path.expanduser('~')
        filename = appname + ".cfg"
        prefix = ''
    return os.path.join(rootname, prefix + filename)


def config_to_options(config):
    """
    Convert ConfigParser instance to argparse.Namespace

    Parameters
    ----------
    config : object
        A ConfigParser instance

    Returns
    -------
    object
        An argparse.Namespace instance
    """
    class Options:
        host=config.get('smtp', 'host', raw=True)
        port=config.getint('smtp', 'port')
        to_addr=config.get('mail', 'to_addr', raw=True)
        from_addr=config.get('mail', 'from_addr', raw=True)
        subject=config.get('mail', 'subject', raw=True)
        encoding=config.get('mail', 'encoding', raw=True)
        username=config.get('auth', 'username')
    opts = Options()
    # format
    opts.from_addr % {'host': opts.host, 'prog': 'notify'}
    opts.to_addr % {'host': opts.host, 'prog': 'notify'}
    return opts


def create_default_config():
    """
    Create default ConfigParser instance
    """
    import codecs
    config = configparser.SafeConfigParser()
    config.readfp(StringIO(DEFAULT_CONFIG))

    # Load user settings
    filename = get_user_config_filename()
    if not os.path.exists(filename):
        from .wizard import setup_wizard
        setup_wizard(config)
    else:
        try:
            fi = codecs.open(filename, 'r', encoding='utf-8')
            config.readfp(fi)
        finally:
            fi.close()
    return config
