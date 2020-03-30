==================
Installing Shuttle
==================

The easiest way to install Shuttle is via pip.

::

    $ pip install pyshuttle

For the versions available, see the `tags on this repository <https://github.com/meherett/shuttle/tags>`_.

Development
===========

We welcome pull requests. To get started, just fork this `github repository <https://github.com/meherett/shuttle>`_, clone it locally, and run:

::

    $ pip install -e . -r requirements.txt

Once you have installed, type ``shuttle`` to verify that it worked:

::

    $ shuttle
    Usage: shuttle [OPTIONS] COMMAND [ARGS]...

      SHUTTLE CLI

      Cross-chain atomic swaps between the networks of two cryptocurrencies.

      LICENCE AGPL-3.0 | AUTHOR Meheret Tesfaye | EMAIL meherett@zoho.com

    Options:
      -v, --version  Show Shuttle version and exit.
      -h, --help     Show this message and exit.

    Commands:
      bitcoin  Select bitcoin cryptocurrency provider.
      bytom    Select bytom cryptocurrency provider.

Dependencies
============

Shuttle has the following dependencies:

* `bytom-wallet-desktop <https://bytom.io/en/wallet/>`_ - tested with version `1.1.0 <https://github.com/Bytom/bytom/releases/tag/v1.1.0>`_
* `pip <https://pypi.org/project/pip/>`_ - To install packages from the Python Package Index and other indexes
* `python3 <https://www.python.org/downloads/release/python-368/>`_ version 3.6 or greater, python3-dev
