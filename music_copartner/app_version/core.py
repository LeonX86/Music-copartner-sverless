"""
app_version

Get version information from ``setup.py`` via ``pkg_resources``.

The concept is taken from this answer

http://stackoverflow.com/a/17638236

written by Martijn Pietersp
"""
import os
import inspect
from pkg_resources import get_distribution
from pkg_resources import DistributionNotFound

__all__ = (
    'get_string_version',
    'get_tuple_version',
    'get_versions',
)

DEFAULT_STRING_NOT_FOUND = 'Please install this application with setup.py'
DEFAULT_TUPLE_NOT_FOUND = (0, 0, 0)


def get_string_version(name,
                       default=DEFAULT_STRING_NOT_FOUND,
                       allow_ambiguous=True):
    """
    Get string version from installed package information.

    It will return :attr:`default` value when the named package is not
    installed.

    Parameters
    -----------
    name : string
        An application name used to install via setuptools.
    default : string
        A default returning value used when the named application is not
        installed yet
    allow_ambiguous : boolean
        ``True`` for allowing ambiguous version information.
        Turn this argument to ``False`` if ``get_string_version`` report wrong
        version.

    Returns
    --------
    string
        A version string or not found message (:attr:`default`)

    Examples
    --------
    >>> import re
    >>> v = get_string_version('app_version', allow_ambiguous=True)
    >>> re.match('^\d+.\d+\.\d+', v) is not None
    True
    >>> get_string_version('distribution_which_is_not_installed')
    'Please install this application with setup.py'
    """
    # get filename of callar
    callar = inspect.getouterframes(inspect.currentframe())[1][1]
    if callar.startswith('<doctest'):
        # called from doctest, find written script file
        callar = inspect.getouterframes(inspect.currentframe())[-1][1]
    # get version info from distribution
    try:
        di = get_distribution(name)
        installed_directory = os.path.join(di.location, name)
        if not callar.startswith(installed_directory) and not allow_ambiguous:
            # not installed, but there is another version that *is*
            raise DistributionNotFound
    except DistributionNotFound:
        return default
    else:
        return di.version


def get_tuple_version(name,
                      default=DEFAULT_TUPLE_NOT_FOUND,
                      allow_ambiguous=True):
    """
    Get tuple version from installed package information for easy handling.

    It will return :attr:`default` value when the named package is not
    installed.

    Parameters
    -----------
    name : string
        An application name used to install via setuptools.
    default : tuple
        A default returning value used when the named application is not
        installed yet
    allow_ambiguous : boolean
        ``True`` for allowing ambiguous version information.

    Returns
    --------
    string
        A version tuple

    Examples
    --------
    >>> v = get_tuple_version('app_version', allow_ambiguous=True)
    >>> len(v) >= 3
    True
    >>> isinstance(v[0], int)
    True
    >>> isinstance(v[1], int)
    True
    >>> isinstance(v[2], int)
    True
    >>> get_tuple_version('distribution_which_is_not_installed')
    (0, 0, 0)
    """
    def _prefer_int(x):
        try:
            return int(x)
        except ValueError:
            return x
    version = get_string_version(name, default=default,
                                 allow_ambiguous=allow_ambiguous)
    # convert string version to tuple version
    # prefer integer for easy handling
    if isinstance(version, tuple):
        # not found
        return version
    return tuple(map(_prefer_int, version.split('.')))


def get_versions(name,
                 default_string=DEFAULT_STRING_NOT_FOUND,
                 default_tuple=DEFAULT_TUPLE_NOT_FOUND,
                 allow_ambiguous=True):
    """
    Get string and tuple versions from installed package information

    It will return :attr:`default_string` and :attr:`default_tuple` values when
    the named package is not installed.

    Parameters
    -----------
    name : string
        An application name used to install via setuptools.
    default : string
        A default returning value used when the named application is not
        installed yet
    default_tuple : tuple
        A default returning value used when the named application is not
        installed yet
    allow_ambiguous : boolean
        ``True`` for allowing ambiguous version information.

    Returns
    --------
    tuple
        A version string and version tuple

    Examples
    --------
    >>> import re
    >>> v1, v2 = get_versions('app_version', allow_ambiguous=True)
    >>> isinstance(v1, str)
    True
    >>> isinstance(v2, tuple)
    True
    >>> get_versions('distribution_which_is_not_installed')
    ('Please install this application with setup.py', (0, 0, 0))
    """
    version_string = get_string_version(name, default_string, allow_ambiguous)
    version_tuple = get_tuple_version(name, default_tuple, allow_ambiguous)
    return version_string, version_tuple


if __name__ == '__main__':
    import doctest
    doctest.testmod()
