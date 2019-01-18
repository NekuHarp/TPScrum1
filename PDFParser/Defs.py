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

_CLI_DESC = 'scientific articles parser'
_CLI_SAVE_TXT = 'Save as text'
_CLI_SAVE_XML = 'Save as XML'
_CLI_HELP_FOLDER = "input folder with PDF files"
_CLI_FOLDER_META = "./documents"

_FLAGS_L = {
    't': ['--text', 'store_true', _CLI_SAVE_TXT],
    'x': ['--xml', 'store_true', _CLI_SAVE_XML]
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

_COUNT_SZ = 20

COUNT = 0

SKIP = ['IEEE TRANSACTIONS ON SPEECH AND AUDIO PROCESSING, VOL. 12, NO. 4, JULY 2004', '401']

REMOV_TITLE = [',', 'and', 'a,*,', 'a,', 'b,1', 'of']
IGNORE_ME = ['in', 'and', 'for']

DISC = ['Discussion']
ACK = ['Acknowledgements', 'ACKNOWLEDGMENT', 'Acknowledgments']
REFS = ['References', 'REFERENCES']
CONCL = ['Conclusion', 'Conclusions', ' Conclusions and future work', 'Conclusions and Future Work', 'CONCLUSIONS AND FURTHER WORK', 'Conclusions and further work', 'Conclusions and future work', 'Conclusion and Future Work', 'IV CONCLUSION']
INTR = ['∗','Introduction', 'I INTRODUCTION', 'Introduction', 'INTRODUCTION', 'Introduction', 'I. I NTRODUCTION']

AUTH_END = ['This article ']
INTREND = ['2', '2.', '2', 'II. SUMMARIZATION WITH TEXT PRESENTATION', '2. Sentence Boundary Detection for MSA', '2 The Skip-gram Model', '2. Core system: SumBasic']
CONCL_END = ['Follow-Up Work']

CORPS = ['2.','2','II.']

_MAX_LEN = 80

_DIGITS = '0123456789.,; ()[]'
_ASCII_TEXT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
