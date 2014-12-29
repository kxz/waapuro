#!/usr/bin/env python
import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test


class Tox(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


setup(
    name='waapuro',
    description='A dead-simple hiragana and katakana romanization library',
    version='1.0',
    author='Kevin Xiwei Zheng',
    author_email='blankplacement+waapuro@gmail.com',
    url='https://github.com/kxz/waapuro',
    license='X11',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries'],
    keywords='japanese kana hiragana katakana romanization',
    packages=find_packages(),
    install_requires=[
        'future'],
    tests_require=[
        'tox'],
    cmdclass={
        'test': Tox})
