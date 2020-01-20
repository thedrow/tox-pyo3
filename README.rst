========
tox-pyo3
========

.. image:: https://img.shields.io/pypi/v/tox-pyo3.svg
    :target: https://pypi.org/project/tox-pyo3
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/tox-pyo3.svg
    :target: https://pypi.org/project/tox-pyo3
    :alt: Python versions

.. image:: https://travis-ci.org/thedrow/tox-pyo3.svg?branch=master
    :target: https://travis-ci.org/thedrow/tox-pyo3
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/thedrow/tox-pyo3?branch=master
    :target: https://ci.appveyor.com/project/thedrow/tox-pyo3/branch/master
    :alt: See Build Status on AppVeyor

Build a rust extension using PyO3 using tox

----

An extremely basic plugin that builds Rust extensions within tox virtualenvs.

Features
--------

* Runs maturin develop


Requirements
------------

* maturin must be installed somewhere in your system
* A rust compiler


Installation
------------

You can install "tox-pyo3" via `pip`_ from `PyPI`_::

    $ pip install tox-pyo3


Usage
-----

* When you set pyo3=true in your testenv this plugin
  automatically detects if Cargo.toml is present and if so, it will compile the
  extension

Example:

```ini
[testenv]
pyo3 = True
```

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `BSD-3`_ license, "tox-pyo3" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _pip: https://pip.pypa.io/en/stable/
.. _PyPI: https://pypi.org/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _BSD-3: https://opensource.org/licenses/BSD-3-Clause
.. _file an issue: https://github.com/thedrow/tox-pyo3/issues