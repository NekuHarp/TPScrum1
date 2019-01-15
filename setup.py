#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
try:
    from setuptools import setup
    from setuptools.command.test import test as Command
except ImportError:
    from distutils.core import setup
    from distutils.cmd import Command

from PDFParser.Version import getVersion, getFullVersion
import sys

dependency_links = ['./misc/cefpython3-66.0-py2.py3-none-any.whl']
install_requires = ['argparse', 'cefpython3']
tests_require = []

class Ver(Command):
    def run(self):
        vers = getFullVersion()
        print(" Version    : %s" % vers.split(" ")[0])
        print("   edition  : %s" % vers.split(" ")[1])
        print("   revision : %s" % vers.split(" ")[2])

class Run(Command):
    def run(self):
        from PDFParser.Client import Client
        c = Client()
        c.run()

class Tests(Command):
    def initialize_options(self):
        Command.initialize_options(self)
        pass
    def finalize_options(self):
        Command.finalize_options(self)
        pass
    def run_tests(self):
        print(self)

cmds = {
    "version": Ver,
    "test": Tests,
    "run": Run,
}

setup(
    name='PDFParser',
    version=getVersion(),
    description="Parse data from scientific articles",
    author="GRANIER Jean-Clair, BOUCHET Lucas, BARRIOL Rémy, WATTIN Tristan, MALEPLATE Bastien",
    author_email='',
    license='Apache-2.0',
    url='https://github.com/NekuHarp/TPScrum1/',
    packages=['PDFParser'],
    # See https://PyPI.python.org/PyPI?%3Aaction=list_classifiers
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Environment :: Other Environment',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: Apache Software License',
                 'Natural Language :: English',
                 'Operating System :: Unix',
                 'Topic :: Text Processing :: Markup :: XML',
                 'Topic :: Text Processing',
                 'Topic :: Scientific/Engineering',
                 'Programming Language :: Python :: 3',
                 ],

    # What does your project relate to?
    keywords='PDF science scientific article',
    install_requires=install_requires,
    dependency_links=dependency_links,
    tests_require=tests_require,
    cmdclass=cmds
)
