# -*- coding: utf-8
"""Unit tests for Waapuro's basic romanization functionality."""
# pylint: disable=missing-docstring


from __future__ import unicode_literals
import unittest

from .. import romanize


class RomanizationTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(romanize('こんにちは'), 'konnitiha')
        self.assertEqual(romanize('コンニチハ'), 'konnitiha')
        self.assertEqual(romanize('がくえん'), 'gakuen')
        self.assertEqual(romanize('ピンぼけ'), 'pinboke')

    def test_youon(self):
        self.assertEqual(romanize('キャンバス'), 'kyanbasu')
        self.assertEqual(romanize('じゃくてん'), 'zyakuten')
        self.assertEqual(romanize('ゃ'), 'ya')

    def test_sokuon(self):
        self.assertEqual(romanize('つっこむ'), 'tukkomu')
        self.assertEqual(romanize('まっちゃ'), 'mattya')
        self.assertEqual(romanize('はやっ'), "haya'")

    def test_chouonpu(self):
        self.assertEqual(romanize('コード'), 'koodo')
        self.assertEqual(romanize('んー'), 'nn')

    def test_syllabic_n(self):
        self.assertEqual(romanize('こんや'), "kon'ya")
        self.assertEqual(romanize('げんあん'), "gen'an")
        self.assertEqual(romanize('にゃんこ'), 'nyanko')

    def test_hepburnish(self):
        self.assertEqual(
            romanize('しじじゃじょちぢつっちっちゃづふ', hepburnish=True),
            'shijijajochijitsutchitchazufu')

    def test_readme_examples(self):
        self.assertEqual(romanize('とおりゃんせ'), 'tooryanse')
        self.assertEqual(romanize('あいづち'), 'aiduti')
        self.assertEqual(romanize('あいづち', hepburnish=True), 'aizuchi')
