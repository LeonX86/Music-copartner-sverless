app_version
==========================
.. image:: https://img.shields.io/travis/lambdalisue/app_version/master.svg?style=flat-square
    :target: http://travis-ci.org/lambdalisue/app_version
    :alt: Build status
.. image:: https://img.shields.io/coveralls/lambdalisue/app_version/master.svg?style=flat-square
    :target: https://coveralls.io/github/lambdalisue/app_version?branch=master 
    :alt: Coverage
.. image:: https://img.shields.io/requires/github/lambdalisue/app_version/master.svg?style=flat-square
    :target: https://requires.io/github/lambdalisue/app_version/requirements/?branch=master
    :alt: Requirements Status
.. image:: https://img.shields.io/pypi/v/app_version.svg?style=flat-square
    :target: https://github.com/lambdalisue/app_version/blob/master/setup.py
    :alt: Version
.. image:: https://img.shields.io/pypi/l/app_version.svg?style=flat-square
    :target: https://github.com/lambdalisue/app_version/blob/master/LICENSE
    :alt: License
.. image:: https://img.shields.io/pypi/format/app_version.svg?style=flat-square
    :target: https://pypi.python.org/pypi/app_version/
    :alt: Format
.. image:: https://img.shields.io/pypi/pyversions/app_version.svg?style=flat-square
    :target: https://pypi.python.org/pypi/app_version/
    :alt: Supported python versions
.. image:: https://img.shields.io/pypi/status/app_version.svg?style=flat-square
    :target: https://pypi.python.org/pypi/app_version/
    :alt: Status

Do you write the version information on ``setup.py`` and ``__init__.py``?

This tiny application allow you to access version information of ``setup.py`` from ``__init__.py``.

Based on `this post <http://stackoverflow.com/questions/17583443/what-is-the-correct-way-to-share-package-version-with-setup-py-and-the-package/17638236#17638236>`_, I wrote this tiny application for convinience.

Check `online documentation <http://python-app_version.readthedocs.org/en/latest/>`_ for more details.

Installation
------------
Use pip_ like::

    $ pip install app_version

.. _pip: https://pypi.python.org/pypi/pip

Usage
-----
The following code is an example ``__init__.py``.

.. code-block:: python

    from app_version import get_versions
    __version__, VERSION = get_versions('your app name')

Then you can access the version string with ``__version__`` and version tuple with ``VERSION``.
The version tuple is useful for comparing versions like

.. code-block:: python

    >>> VERSION = (0, 1, 2)
    >>> VERSION > (0, 1, 0)
    True
    >>> VERSION > (0, 1, 1)
    True
    >>> VERSION > (0, 1, 2)
    False


