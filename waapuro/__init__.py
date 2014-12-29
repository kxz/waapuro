# -*- coding: utf-8
"""The Waapuro hiragana and katakana romanization library."""


from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *  # pylint: disable=redefined-builtin,wildcard-import

import re
import unicodedata


#: Regex matching Unicode names of basic kana.
BASIC_KANA_NAME = re.compile(r'^(?:HIRAG|KATAK)ANA LETTER ([^ ]+)$')

#: Regex matching Unicode names of small kana.
SMALL_KANA_NAME = re.compile(r'^(?:HIRAG|KATAK)ANA LETTER SMALL ([^ ]+)$')

def _build_tables():
    """Use the Unicode character database to build basic and small kana
    dictionaries, and return the pair as a tuple."""
    basic_kana = dict()
    small_kana = dict()
    for codepoint in range(0x3040, 0x3100):
        kana = chr(codepoint)
        name = unicodedata.name(kana, '')
        basic_kana_match = BASIC_KANA_NAME.match(name)
        if basic_kana_match is not None:
            romaji = basic_kana_match.group(1).lower()
            basic_kana[kana] = romaji
            continue
        small_kana_match = SMALL_KANA_NAME.match(name)
        if small_kana_match is not None:
            small_kana[kana] = small_kana_match.group(1).lower()
    return basic_kana, small_kana

#: Simple lookup tables for romanizations of basic and small kana.
BASIC_KANA, SMALL_KANA = _build_tables()

#: A table of single-kana replacements from Nihon-shiki to make
#: romanizations look more like Hepburn.
HEPBURNISH_REPLACEMENTS = {
    'si': 'shi',
    'zi': 'ji',
    'zya': 'ja',
    'zyo': 'jo',
    'ti': 'chi',
    'di': 'ji',
    'tu': 'tsu',
    'du': 'zu',
    'hu': 'fu',
}


def romanize(kana_string, hepburnish=False):
    """Return a romanized version of *kana_string* as a Unicode string.

    By default, romanization is performed according to ISO 3602 Strict
    (Nihon-shiki) with long vowels expanded (e.g., *ou* or *oo* instead
    of *ô*).  If *hepburnish* is True, the following changes are made:

    - *si* → *shi*
    - *sya* → *sha*
    - *syo* → *sho*
    - *zi* → *ji*
    - *zya* → *ja*
    - *zyo* → *jo*
    - *ti* → *chi*
    - *tya* → *cha*
    - *tyo* → *cho*
    - *di* → *ji*
    - *tu* → *tsu*
    - *cchi* → *tchi*
    - *ccha* → *tcha*
    - *ccho* → *tcho*
    - *du* → *zu*
    - *hu* → *fu*

    Waapuro is not capable of identifying long vowels or nonstandard
    pronunciations (such as *wa* instead of *ha* for the topic marker).

    This function's behavior on strings containing non-kana characters
    is currently undefined.  In practice, such characters will usually
    be left intact, but this should not be relied on.
    """
    romaji_list = []
    sokuon = False
    for kana in kana_string:
        if kana in ('っ', 'ッ'):
            sokuon = True
            continue
        if kana == 'ー':
            if romaji_list:
                romaji_list.append(romaji_list[-1][-1])
            else:
                romaji_list.append('-')
            continue
        if kana in SMALL_KANA:
            romaji = SMALL_KANA[kana]
            if romaji_list:
                # Chop off the last character of the previous romaji
                # in order to accommodate the palatalization.
                romaji_list[-1] = romaji_list[-1][:-1]
                # Transform *zya* into Hepburnish *ja*.
                if (hepburnish and romaji[0] == 'y' and
                        romaji_list[-1] in ('ch', 'tch', 'sh', 'ssh', 'j')):
                    romaji = romaji[1:]
            romaji_list.append(romaji)
            continue
        romaji = BASIC_KANA.get(kana, kana)
        if hepburnish:
            romaji = HEPBURNISH_REPLACEMENTS.get(romaji, romaji)
        if sokuon:
            if hepburnish and romaji[0] == 'c':
                romaji = 't' + romaji
            else:
                romaji = romaji[0] + romaji
            sokuon = False
        if (romaji_list and romaji_list[-1] == 'n' and
                romaji[0] in ('a', 'i', 'u', 'e', 'o', 'y')):
            romaji = "'" + romaji
        romaji_list.append(romaji)
    if sokuon:
        romaji_list.append("'")
    return ''.join(romaji_list)
