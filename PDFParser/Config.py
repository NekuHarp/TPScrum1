# -*- coding: utf-8 -*-

from . import Defs as _D

import pickle
import os

wd = _D.wd
outf = _D.outF
path = _D.CONFIG_DIR
conff = _D.CONFIG_FILE

class Config:
    def __init__(self, fname=conff, path=path, wd=wd, outF=outf):
        self.fname = fname
        self.path = path
        self.wd = wd
        self.outF = outF
        self.outD = '{}/{}'.format(self.wd, self.outF)
        self.DO = _D._DO
        self.XML_TAGS = _D._XML_TAGS
        self.TXT_TAGS = _D._TXT_TAGS

    def getXMLTags(self):
        return self.XML_TAGS

    def getXMLTag(self, val):
        return '' if not val in self.XML_TAGS else self.XML_TAGS[val]

    def setXMLTag(self, key, val):
        if key in self.XML_TAGS:
            self.XML_TAGS[key] = val
            return True
        return False

    def getTXTTags(self):
        return self.TXT_TAGS

    def getTXTTag(self, val):
        return '' if not val in self.TXT_TAGS else self.TXT_TAGS[val]

    def setTXTTag(self, key, val):
        if key in self.TXT_TAGS:
            self.TXT_TAGS[key] = val
            return True
        return False

    def getDoTags(self):
        return self.DO

    def getDoTag(self, val):
        return '' if not val in self.DO else self.DO[val]

    def setDoTag(self, key, val):
        if key in self.DO:
            self.DO[key] = val
            return True
        return False

    def set(self, dict, key, value):
        pass

    def saveConfig(self, DO={}, XML_TAGS={}, TXT_TAGS={} , outF='', wd='', outD='', fname=""):
        if(DO == {}): DO = self.DO
        if(XML_TAGS == {}): XML_TAGS = self.XML_TAGS
        if(TXT_TAGS == {}): TXT_TAGS = self.TXT_TAGS
        if(outF == ''): outF = self.outF
        if(wd == ''): wd = self.wd
        if(outD == ''): outD = self.outD
        path = self.path
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        if not os.path.exists(self.path):
            path = "."
        if(fname==""):
            _out = open(path+"/"+self.fname, 'wb')
        else:
            _out = open(path+"/"+fname, 'wb')
        pickle.dump(DO, _out)
        pickle.dump(XML_TAGS, _out, -1)
        pickle.dump(TXT_TAGS, _out, -1)
        pickle.dump(wd, _out, -1)
        pickle.dump(outF, _out, -1)
        pickle.dump(outD, _out, -1)
        _out.close()

    def loadConfig(self, fname=conff):
        if not os.path.isfile(fname):
            self.saveConfig(fname)
        else:
            _in = open(fname, 'rb')
            try:
                W_DO = pickle.load(_in)
                [self.setDoTag(i, W_DO[i]) for i in W_DO]
                W_XML = pickle.load(_in)
                [self.setXMLTag(i, W_XML[i]) for i in W_XML]
                W_TXT = pickle.load(_in)
                [self.setTXTTag(i, W_TXT[i]) for i in W_TXT]
                self.wd = pickle.load(_in)
                self.outF = pickle.load(_in)
                self.outD = '{}/{}'.format(self.wd, self.outF)
            except:
                pass
            _in.close()
        r = {'DO':self.DO, 'XML':self.XML_TAGS, 'TXT':self.TXT_TAGS, 'wd':self.wd, 'outF':self.outF, 'outD':self.outD}
        return r
