Waapuro
=======

A dead-simple hiragana and katakana romanization library for Python 2.7
and 3.4+.

By default, romanization is performed according to `ISO 3602 Strict
(Nihon-shiki) <nihonshiki_>`_ with long vowels expanded (e.g., *ou* or
*oo* instead of *ô*):

>>> from __future__ import unicode_literals
>>> import waapuro
>>> waapuro.romanize('とおりゃんせ')
'tooryanse'

Passing the *hepburnish* option replaces some of the individual kana
romanizations with more Hepburn_-like variants:

>>> waapuro.romanize('あいづち')
'aiduti'
>>> waapuro.romanize('あいづち', hepburnish=True)
'aizuchi'

To install, just use::

    $ pip install waapuro

Report bugs and make feature requests on `Waapuro's GitHub project
page <github_>`_.

.. _github: https://github.com/kxz/waapuro
.. _hepburn: https://en.wikipedia.org/wiki/Hepburn_romanization
.. _nihonshiki: https://en.wikipedia.org/wiki/Nihon-shiki_romanization
