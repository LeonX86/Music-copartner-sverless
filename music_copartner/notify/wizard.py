# coding=utf-8
"""
A notify setup wizard module
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'

class ValidationError(Exception):
    pass

def validate_int(x):
    try:
        return int(x)
    except TypeError:
        raise ValidationError("A natural number is required.")

def validate_email(x):
    from validate_email import validate_email
    if not validate_email(x):
        raise ValidationError("A valid email address is required.")
    return x

def console_input(default, validation=None, allow_empty=False):
    """
    Get user input value from stdin

    Parameters
    ----------
    default : string
        A default value. It will be used when user input nothing.
    validation : callable
        A validation function. The validation function must raise an error
        when validation has failed.

    Returns
    -------
    string or any
        A user input string or validated value
    """
    value = input("> ") or default
    if value == "" and not allow_empty:
        print("Invalid: Empty value is not permitted.")
        return console_input(default, validation)
    if validation:
        try:
            return validation(value)
        except ValidationError as e:
            print("Invalid: ", e)
            return console_input(default, validation)
    return value

def setup_wizard(config):
    from notify.compat import keyring
    print()
    print("#" * 50)
    print("#", "#".rjust(48))
    print("#", "notify setup wizard".center(46), "#")
    print("#", "#".rjust(48))
    print("#" * 50)
    print()
    print("Note: square bracket enclosed text indicate the current value")
    print()

    # SMTP section
    host = config.get('smtp', 'host', raw=True)
    port = config.get('smtp', 'port', raw=True)
    print("1. Please enter mail user agent host address [%s]" % host)
    host = console_input(host)
    print("2. Please enter mail user agent port number [%s]" % port)
    print("|")
    print("| The following port numbers are usually used.")
    print("| - 25  : A default SMTP port")
    print("| - 465 : A default SMTP over SSL port")
    print("| - 587 : A default submission port")
    print("|")
    port = console_input(port, validate_int)

    # Mail section
    from_addr = config.get('mail', 'from_addr', raw=True)
    to_addr = config.get('mail', 'to_addr', raw=True)
    subject = config.get('mail', 'subject', raw=True)
    encoding = config.get('mail', 'encoding', raw=True)
    print("3. Please enter an email address for 'from' [%s]" % from_addr)
    from_addr = console_input(from_addr, validate_email)
    print("4. Please enter an email address for 'to' [%s]" % to_addr)
    to_addr = console_input(to_addr, validate_email)
    print("5. Please enter an email subject [%s]" % subject)
    print("|")
    print("| The following special string are available.")
    print("| - %(prog)s   : A program name executed.")
    print("| - %(status)s : A exit status of executed.")
    print("|")
    subject = console_input(subject)
    print("6. Please enter an email encoding [%s]" % encoding)
    encoding = console_input(encoding)

    # Auth section
    username = config.get('auth', 'username', raw=True)
    password = keyring.get_password('notify', username) or ""
    print("7. Please enter an username for authentication [%s]" % username)
    print("|")
    print("| To remove username, input 'REMOVE'")
    print("|")
    username = console_input(username, allow_empty=True)
    if username == 'REMOVE':
        username = ""
    print("8. Please enter an password for authentication")
    print("|")
    print("| To remove password, input 'REMOVE'")
    print("|")
    password = console_input(password, allow_empty=True)
    if password == "REMOVE":
        password = ""

    # save into config
    config.set('smtp', 'host', host)
    config.set('smtp', 'port', str(port))
    config.set('mail', 'from_addr', from_addr)
    config.set('mail', 'to_addr', to_addr)
    config.set('mail', 'subject', subject)
    config.set('mail', 'encoding', encoding)
    config.set('auth', 'username', username)
    # do not store password in config file
    if username:
        if password:
            keyring.set_password('notify', username, password)
        elif keyring.get_password('notify', username):
            keyring.delete_password('notify', username)

    # save config
    import os
    import codecs
    from notify.conf import get_user_config_filename
    filename = get_user_config_filename()
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    try:
        fo = codecs.open(filename, 'wb', 'utf-8')
        config.write(fo)
    finally:
        fo.close()

if __name__ == '__main__':
    setup_wizard(None)
