# coding=utf-8
"""
Compatibility module
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
try:
    # pip install keyring
    import keyring
except ImportError:
    # use alternative keyring which use plaintext.
    # it is strongly not recommended
    import os
    from notify.utils.plaintext_keyring import PlaintextKeyring
    from notify.conf import get_user_config_filename
    filename = os.path.splitext(get_user_config_filename())[0]
    filename = filename + ".keyring"
    keyring = PlaintextKeyring(filename)

try:
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import formatdate
except ImportError:
    # old way
    from email.Header import Header
    from email.MIMEText import MIMEText
    from email.Utils import formatdate
