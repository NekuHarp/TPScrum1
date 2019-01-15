# -*- coding: utf-8 -*-

import argparse
import os

from .Client import Client as _C

class Cli:
    def __init__(self):
        self.p = argparse.ArgumentParser(description='scientific articles parser')
        self.p.add_argument("folder",
        help="input file with two matrices", metavar="./documents",
        type=lambda x: x if os.path.isdir(x) else '.')
        self.p.add_argument('-t', '--text', action='store_true',
        help='Save as text')
        self.p.add_argument('-x', '--xml', action='store_true',
        help='Save as XML')

        self.c = _C()
        self.doXML = self.c.doXML
        self.doTXT = self.c.doTXT

    def progress(pos, total, sz):
        step = float(pos)/total
        f = step*sz
        f = int(f)
        sys.stdout.write('\r|'+'[7m [27m'*f + ' '*(sz-f)+'| [7m[{:>4.0%}][27m'.format(step))
        sys.stdout.flush()

    def status(str):
        sys.stdout.write(u"\u001b[" + "A") # Move up
        sys.stdout.write('\r'+str+'\n')
        sys.stdout.flush()

    def main(self):
        args = self.p.parse_args()
        if(args.xml):
            self.doXML(args.folder)
        if(args.text):
            self.doTXT(args.folder)
        print(args)
