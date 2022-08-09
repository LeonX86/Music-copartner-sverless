from app_version.core import get_versions
from app_version.core import get_tuple_version
from app_version.core import get_string_version

__version__, VERSION = get_versions('app_version')


__all__ = (
    '__version__',
    'VERSION',
    'get_versions',
    'get_tuple_version',
    'get_string_version',
)
