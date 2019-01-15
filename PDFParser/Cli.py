# -*- coding: utf-8 -*-

import subprocess
import argparse
import os
import sys

from .Client import Client as _C
from . import Defs as _D

APP_NAME = _D.APP_NAME
_COUNT_SZ = _D._COUNT_SZ
_MAX_LEN = _D._MAX_LEN
_TXT = _D._TXT
_APP = _D._APP
XML = _D._XML
COUNT = 0
HELP_MSG = _D.HELP_MSG
_CLI_DESC = _D._CLI_DESC
_CFLAG = _D._CFLAG
_FLAGS = _D._FLAGS
_FLAGS_L = _D._FLAGS_L
_SFLAG = _D._SFLAG
_HELP_FOLDER = _D._CLI_HELP_FOLDER
_FOLDER_META = _D._CLI_FOLDER_META

class Cli:
    def __init__(self):
        self.p = argparse.ArgumentParser(description=_CLI_DESC)
        self.p.add_argument("folder",
        help=_HELP_FOLDER, metavar=_FOLDER_META,
        type=lambda x: x if os.path.isdir(x) else '.')
        for f in _CFLAG:
            self.p.add_argument(_SFLAG+f, _FLAGS_L[f][0], action=_FLAGS_L[f][1],
            help=_FLAGS_L[f][2])
        self.c = _C()
        #self.doXML = self.c.doXML
        #self.doTXT = self.c.doTXT

    def progress(self, pos, total, sz):
        step = float(pos)/total
        f = step*sz
        f = int(f)
        sys.stdout.write('\r|'+'[7m [27m'*f + ' '*(sz-f)+'| [7m[{:>4.0%}][27m'.format(step))
        sys.stdout.flush()

    def status(self, str):
        sys.stdout.write(u"\u001b[" + "A") # Move up
        sys.stdout.write('\r'+str+'\n')
        sys.stdout.flush()

    def _prepare(self, wd):
        self.c.setOut(wd)
        return self.c.ls(wd)

    def do(self, wd, xml = XML):
        gl = self._prepare(wd)
        COUNT = len(gl)
        pos = 0
        for g in gl:
            pos += 1
            self.progress(pos, COUNT, _COUNT_SZ)
            fnam = os.path.basename(g)
            if len(fnam)+4>_MAX_LEN: fnam = fnam[:(_MAX_LEN-4-3)]+"..."
            else: fnam += ' '*(_MAX_LEN-4-len(fnam))
            self.status(' > {}'.format(fnam))
            Fname = '{}.{}'.format(g[:-4], _TXT)
            if not os.path.isfile(Fname):
                p = subprocess.Popen([_APP , g , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
                p.wait()
            self.c.parser(Fname, xml)
        print('\n'+HELP_MSG[3])

    def main(self):
        args = self.p.parse_args()

        print('[100m {} [49m\n'.format(APP_NAME))

        if(args.xml):
            self.do(args.folder, True)
        if(args.text):
            self.do(args.folder, False)
