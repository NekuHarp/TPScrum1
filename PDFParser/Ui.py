# -*- coding: utf-8 -*-

import argparse
import os

class Ui:
    def __init__(self):
        self.p = argparse.ArgumentParser(description='scientific articles parser')
        self.p.add_argument("folder",
        help="input file with two matrices", metavar="./documents",
        type=lambda x: x if os.path.isdir(x) else '.')
        self.p.add_argument('-t', '--text', action='store_true',
        help='Save as text')
        self.p.add_argument('-x', '--xml', action='store_true',
        help='Save as XML')

    def main(self):
        args = self.p.parse_args()
        XML = args.xml
        if(XML):
            print('XML')
            _EOUT = 'xml'
        Text = args.text
        print(args)
