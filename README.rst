==========
paunch-dir
==========

.. image:: https://img.shields.io/pypi/v/paunch-dir.svg
    :target: https://pypi.python.org/pypi/paunch-dir

.. image:: https://travis-ci.org/starofrainnight/paunch-dir.svg
    :target: https://travis-ci.org/starofrainnight/paunch-dir.html

.. image:: https://ci.appveyor.com/api/projects/status/github/starofrainnight/paunch-dir?svg=true
    :target: https://ci.appveyor.com/project/starofrainnight/paunch-dir

An algorithm to generate a path from file name which directory structure could
store mass files

You could generated directory structure (from a uuid file name) just like:

::

    ├── 02
    │   └── 9d
    │       └── 5b
    │           └── cb7c89776a923d6050ff9cffcf1333284f.jpg
    |               # Original file name : 029d5bcb7c89776a923d6050ff9cffcf1333284f.jpg
    ├── 03
    │   ├── 2b
    │   │   └── f9
    │   │       └── 7cdb028c51ec56ec53cbe34946525a3e37.jpg
    │   └── f9
    │       └── 4d
    │           └── 9458a9ee5396911268b0da6b3552f154e8.jpg
    ...

It's ineffectively for file system parse large number files in same directory.
And there have limit files that could be sotre in a directory depends on
different file system format. You will see it's very slow if you open a
directory with hundreds of thousands files in file browser. Separate them into
different directory with specific algorithm that could greatly improve
efficiency when parse those files.

Usage
--------


::

    from paunchdir import PaunchDir

    # Generate path from uuid file name
    pdir = PaunchDir(".")
    print(pdir.compose('032bf97cdb028c51ec56ec53cbe34946525a3e37.jpg'))
    # ==> "./03/2b/f9/7cdb028c51ec56ec53cbe34946525a3e37.jpg"

    # Decompose uuid file name from a path
    print(pdir.decompose("./03/2b/f9/7cdb028c51ec56ec53cbe34946525a3e37.jpg"))
    # ==> "032bf97cdb028c51ec56ec53cbe34946525a3e37.jpg"

    # Generate path from uuid file name with one level (Just like what the git
    # store it's objects)
    pdir = PaunchDir("./objects", levels=1)
    print(pdir.compose('032bf97cdb028c51ec56ec53cbe34946525a3e37'))
    # ==> "./03/2bf97cdb028c51ec56ec53cbe34946525a3e37"

License
-------

This library license under Apache-2.0

Credits
---------

This package was created with Cookiecutter_ and the `PyPackageTemplate`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`PyPackageTemplate`: https://github.com/starofrainnight/rtpl-pypackage

