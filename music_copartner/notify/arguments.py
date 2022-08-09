# coding=utf-8
"""
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import sys
import optparse

def split_arguments(args):
    """
    Split specified arguments to two list.

    This is used to distinguish the options of the program and
    execution command/arguments.

    Parameters
    ----------
    args : list
        Command line arguments

    Returns
    -------
    list : options, arguments
        options indicate the optional arguments for the program and
        arguments indicate the execution command/arguments
    """
    prev = False
    for i, value in enumerate(args[1:]):
        if value.startswith('-'):
            prev = True
        elif prev:
            prev = False
        else:
            return args[:i+1], args[i+1:]
    return args, []

def parse_arguments(args, config):
    """
    Parse specified arguments via config

    Parameters
    ----------
    args : list
        Command line arguments
    config : object
        ConfigParser instance which values are used as default values of
        options

    Returns
    -------
    list : arguments, options
        options indicate the return value of ArgumentParser and arguments
        indicate the execution command/arguments
    """
    import notify
    from .conf import config_to_options
    opts = config_to_options(config)

    usage = ("%(prog)s "
             "[-h] [-t TO_ADDR] [-f FROM_ADDR] [-e ENCODING] [-s SUBJECT]\n"
             "              "
             "[-o HOST] [-p PORT] [--username USERNAME] [--password PASSWORD]\n"
             "              "
             "[--setup] [--check] COMMAND ARGUMENTS") % {'prog': "notify"}
    description = """
    Call COMMAND with ARGUMENTS and send notification email to TO_ADDR
    """
    parser = optparse.OptionParser(
            usage=usage,
            description=description,
            version=notify.__version__)
    parser.add_option('-t', '--to-addr',
                      default=opts.to_addr,
                      help=('Destination of the email.'))
    parser.add_option('-f', '--from-addr',
                      default=opts.from_addr,
                      help=('Source of the email.'))
    parser.add_option('-s', '--subject',
                      default=opts.subject,
                      help=('Subject of the email'))
    parser.add_option('-e', '--encoding',
                      default=opts.encoding,
                      help=('Encoding of the email'))
    parser.add_option('-o', '--host',
                      default=opts.host,
                      help=('Host address of MUA'))
    parser.add_option('-p', '--port', type='int',
                      default=opts.port,
                      help=('Port number of MUA'))
    parser.add_option('--username',
                      default=opts.username,
                      help=('Username for authentication'))
    parser.add_option('--password',
                      help=('Password for authentication'))
    parser.add_option('--setup', default=False,
                      action='store_true',
                      help=('Setup %(prog)s configuration'))
    parser.add_option('--check', default=False,
                      action='store_true',
                      help=('Send %(prog)s configuration via email for '
                            'checking. Only for Unix system.'))

    # display help and exit
    if len(args) == 1:
        parser.print_help()
        sys.exit(0)
    else:
        # translate all specified arguments to unicode
        if sys.version_info < (3,):
            encoding = sys.stdout.encoding
            args = [str(x, encoding) for x in args]

        # split argv to two array
        lhs, rhs = split_arguments(args)

        # parse options
        opts = parser.parse_args(args=lhs[1:])[0]
        return rhs, opts
