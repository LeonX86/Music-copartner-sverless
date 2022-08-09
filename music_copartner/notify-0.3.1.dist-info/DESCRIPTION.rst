notify
==========================
.. image:: https://secure.travis-ci.org/lambdalisue/notify.svg?branch=master
    :target: http://travis-ci.org/lambdalisue/notify
    :alt: Build status

.. image:: https://coveralls.io/repos/lambdalisue/notify/badge.svg?branch=master
    :target: https://coveralls.io/r/lambdalisue/notify/
    :alt: Coverage

.. image:: https://img.shields.io/pypi/dm/notify.svg
    :target: https://pypi.python.org/pypi/notify/
    :alt: Downloads

.. image:: https://img.shields.io/pypi/v/notify.svg
    :target: https://pypi.python.org/pypi/notify/
    :alt: Latest version

.. image:: https://img.shields.io/pypi/format/notify.svg
    :target: https://pypi.python.org/pypi/notify/
    :alt: Format

.. image:: https://img.shields.io/pypi/status/notify.svg
    :target: https://pypi.python.org/pypi/notify/
    :alt: Status

.. image:: https://img.shields.io/pypi/l/notify.svg
    :target: https://pypi.python.org/pypi/notify/
    :alt: License

.. image:: https://img.shields.io/pypi/pyversions/notify.svg
    :target: https://pypi.python.org/pypi/notify/
    :alt: Support version

Notify process termination via email.
It support Python 2.4 and later (Python 2.4 and Python 2.5 were manually tested,
so it might not work).

Installation
------------
Use pip_ like::

    $ pip install notify

.. _pip:  https://pypi.python.org/pypi/pip

Additionally, if you would like to use a mail user agent which requires authentication, installing keyring is strongly recommended::

    $ pip install keyring

Usage
--------
1.  Running *notify* with the following command will start a setup wizard the first time.
    ::

        $ notify

2.  Follow the setup wizard instructions.

3.  Check with the following command (Only for Unix system)
    ::

        $ notify --check

4.  Sample usage of *notify*
    ::

        $ notify really_havy_process -a -b --options
        $ notify -t different@address.com really_havy_process -a -b --options


