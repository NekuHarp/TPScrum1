# -*- coding: utf-8 -*-

from .Version import getFullVersion

VERSION = getFullVersion()

VAR = "b"

APP_NAME = 'PDF Parser 1.1'
HELP_MSG = ['Creating output folder . . .','','','Tasks complete !']

outF = 'out'
wd = './dossier/'

_APP = 'pdftotext'
_EXT = 'pdf'
_TXT = 'txt'
_EOUT = 'txt'
_DESC = 'desc'
_XML = True

CONFIG_DIR = './config/'
CONFIG_FILE = 'config.pak'

PDF_HEADER = "%PDF-"

_XML_TAGS = {
    '_ARTICLE' : 'article',
    '_PREAMBULE' : 'preambule',
    '_TITRE' : 'titre',
    '_AUTEUR' : 'auteur',
    '_ABSTRACT' : 'abstract',
    '_BIBLIO' : 'biblio',
    '_ACK' : 'acknowledgements',
    '_REFS' : 'references',
    '_INTR' : 'introduction',
    '_CORP' : 'corps',
    '_DISC' : 'discussion',
    '_CONCL' : 'conclusion'
}

_TXT_TAGS = {
    '_HEADER' : '[PDF PARSER {}]'.format(VERSION),
    '_ARTICLE' : '\n[ARTICLE]\n',
    '_PREAMBULE' : '\n[PREAMBULE]\n',
    '_TITRE' : '\n[TITRE]\n',
    '_AUTEUR' : '\n[AUTEUR]\n',
    '_ABSTRACT' : '\n[ABSTRACT]\n',
    '_BIBLIO' : '\n[BIBLIO]\n',
    '_ACK' : '\n[ACKNOWLEDGEMENTS]\n',
    '_REFS' : '\n[REFERENCES]\n',
    '_INTR' : '\n[INTRODUCTION]\n',
    '_CORP' : '\n[CORPS]\n',
    '_DISC' : '\n[DISCUSSION]\n',
    '_CONCL' : '\n[CONCLUSION]\n'
}

_HEADER = "[PDF PARSER {}]".format(VERSION)

_DO = {
    '_HEADER' : True,
    '_PREAMBULE' : True,
    '_TITRE' : True,
    '_AUTEUR' : True,
    '_ABSTRACT' : True,
    '_BIBLIO' : True,
    '_ACK' : False,
    '_REFS' : False,
    '_INTR' : True,
    '_CORP' : True,
    '_DISC' : True,
    '_CONCL' : True
}

_CFLAG = ['t', 'x']
_SFLAG = '-'
_FLAGS = [_SFLAG+i for i in _CFLAG]

HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
}
