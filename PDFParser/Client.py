# -*- coding: utf-8 -*-

from . import Defs as _D
from .Parser import Parser as _P

class Client:
    def __init__(self):
        self.id = 4
        self.p = _P()
        pass

    def doXML(self, folder):
        _EOUT = 'xml'
        print(_EOUT, folder)

    def doTXT(self, folder):
        _EOUT = 'txt'
        print(_EOUT, folder)

    def setOut(self, wd):
        self.p.setWD(wd)

    def ls(self, wd):
        gl = self.p.listDir(wd)
        gl = [g.replace('\\','/') for g in gl]
        return gl

    def parser(self, Fname, xml):
        return self.p.parser(Fname, xml)

    def run(self):
        print("Client {} : {} ".format(self.p.parse("-{}".format(self.id)), _D.VAR))
        self.cli.main()
