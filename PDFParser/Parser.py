# -*- coding: utf-8 -*-

import re
import sys
import glob
import os
import subprocess

from .Config import Config
from . import Defs as _D

#TODO: move thoses out
outF = _D.outF
wd = _D.wd
_XML_TAGS = _D._XML_TAGS
_TXT_TAGS = _D._TXT_TAGS
_DO = _D._DO
_XML = _D._XML
_TXT = _D._TXT
_APP = _D._APP
CONFIG_DIR = _D.CONFIG_DIR
PDF_HEADER = _D.PDF_HEADER
HTML_ESCAPE_TABLE= _D.HTML_ESCAPE_TABLE

SKIP = _D.SKIP
REMOV_TITLE = _D.REMOV_TITLE
IGNORE_ME = _D.IGNORE_ME
DISC = _D.DISC
ACK = _D.ACK
REFS = _D.REFS
CONCL = _D.CONCL
INTR = _D.INTR
AUTH_END = _D.AUTH_END
INTREND = _D.INTREND
CONCL_END = _D.CONCL_END
CORPS = _D.CORPS
_DIGITS = _D._DIGITS
_ASCII_TEXT = _D._ASCII_TEXT
_DESC = _D._DESC


class Parser:
    def __init__(self, wd='.', outf = outF):
        self.name = "PDF"
        self.wd = wd
        self.outF = outf
        self.outD = '{}/{}'.format(self.wd, self.outF)

        self.conf = Config()
        self.XML = _XML
        self.XML_TAGS = _XML_TAGS
        self.TXT_TAGS = _TXT_TAGS
        self.DO = _DO

        self.loadConfig()
        self.checkDir()

    def checkDir(self):
        if not os.path.exists(self.outD):
            os.makedirs(self.outD)

    def _update(self):
        self.outD = '{}/{}'.format(self.wd, self.outF)
        self.checkDir()

    def getWD(self):
        return self.wd

    def getOutF(self):
        return self.outF

    def setWD(self, wd):
        if os.path.exists(wd):
            self.wd = wd
            self._update()
            return True
        else:
            return False

    def setOut(self, outf):
        self.outF = outf
        # if not os.path.exists(self.outF):
            # os.makedirs(self.outF)
        self._update()
        return True

    def _updateConfig(self, r):
        #'DO':W_DO, 'XML':W_XML, 'TXT':W_TXT, 'wd':self.wd, 'outF':self.outF, 'outD':self.outD
        self.DO = r['DO']
        self.XML_TAGS = r['XML']
        self.TXT_TAGS = r['TXT']
        self.outF = r['outF']
        self.wd = r['wd']
        self.outD = r['outD']

        self._update()

    def loadConfig(self, fname="config.pak"):
        # if not os.path.isfile(fname):
        #     print("RECREATE")
        #     self.saveConfig(fname)
        r = self.conf.loadConfig(fname);
        self._updateConfig(r)

    def saveConfig(self, fname="config.pak"):
        #   print(self.DO, self.XML_TAGS, self.TXT_TAGS, self.outF, self.wd, self.outD, fname)
        self.conf.saveConfig(self.DO, self.XML_TAGS, self.TXT_TAGS, self.outF, self.wd, self.outD, fname)
        #   print(self.DO, self.XML_TAGS, self.TXT_TAGS, self.outF, self.wd, self.outD, fname)

        #print("TODO: save")

    def checkPDF(self, fname):
        try:
            fichier = open(fname, "r", errors='ignore')
            for l in fichier:
                if l.startswith(PDF_HEADER):
                    return True
                else:
                    return False
        except:
            return False
        return True

    def listDir(self, wd=wd):
        if wd == '':
            wd = self.wd
        if os.path.exists(wd):
            gl = glob.glob('{}/*.{}'.format(wd, "pdf"))
            gl = [g.replace('\\','/') for g in gl]
            gl = [g for g in gl if self.checkPDF(g)]
            return gl
        else:
            return []

    def fromTexttoXML(self, fname, q=''):
        Fname = '{}.{}'.format(fname[:-4], _TXT)
        if not os.path.isfile(Fname):
            if not os.path.isfile(fname):
                return False
            else:
                p = subprocess.Popen([_APP , fname , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
                p.wait()
        try:
            r = self.parser(Fname, xml=True, outf=self.outF)
        except:
            r = ''
        if q!='': q.put(r)
        return r

    def fromTexttoTXT(self, fname, q=''):
        Fname = '{}.{}'.format(fname[:-4], _TXT)
        if not os.path.isfile(Fname):
            if not os.path.isfile(fname):
                return False
            else:
                p = subprocess.Popen([_APP , fname , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
                p.wait()
        try:
            r = self.parser(Fname, xml=False, outf=self.outF)
        except:
            r = ''
        if q!='': q.put(r)
        return r

    def fromPDFtoXML(self, fname, q=''):
        Fname = '{}.{}'.format(fname[:-4], _TXT)
        if not self.checkPDF(fname): return ''
        p = subprocess.Popen([_APP , fname , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
        p.wait()
        try:
            r = self.parser(Fname, xml=True, outf=self.outF)
        except:
            r = ''
        if q!='': q.put(r)
        return r

    def fromPDFtoTXT(self, fname, q=''):
        Fname = '{}.{}'.format(fname[:-4], _TXT)
        if not self.checkPDF(fname): return ''
        p = subprocess.Popen([_APP , fname , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
        p.wait()
        try:
            r = self.parser(Fname, xml=False, outf=self.outF)
        except:
            r = ''
        if q!='': q.put(r)
        return r

    def parseDir(self, wd, xml=True):
        if os.path.exists(wd):
            gl = glob.glob('{}/*.{}'.format(wd, _EXT))
            for g in gl:
                if(xml):
                    self.fromPDFtoXML(g)
                else:
                    self.fromTexttoXML(g)

    def html_escape(self, raw):
        return "".join(HTML_ESCAPE_TABLE.get(c,c) for c in raw)

    def sanitize_body(self, raw):
        try:
            return ' '.join(("\n".join([i for i in raw.split("\n") if len(i)>4 and not (len(i) == len([j for j in i if j in _DIGITS]))])).split(' '))
        except:
            return raw

    def parser(self, Fname, xml='', outf=outF):
        inW = False
        inR = False
        inT = True
        inR = False
        inK = False
        inC = True
        inI = False

        inCo = False

        if(xml == ''):
            xml = self.XML
        else:
            if(xml):
                self.XML = True
                _EOUT = 'xml'
            else:
                self.XML = False
                _EOUT = 'txt'

        inB = 0 # 0 out, 'r' ref, 'a' ack ...
        inBC = 0

        regex = "Abstract.*\n"
        rregex = "^References\n"
        rfregex = "References\n"
        uregex = "www.*.*"
        vregex = "(VOL[.|UME.]*)(( \d*))*"

        endIntroReg = "(2|II)(\.| |)( |)(\w+|)\n" #TODO : end intro with this

        kireg = "^((Keywords:)|(Index Terms[—]*))"

        nreg = "^\d\d{0,}$"

        unreg = "[\u000c]*\d[0-9]+\n"

        wTilte = False

        old_regex = "Abstract[.—]*\n"
        old_rregex = "References\n"
        old_kregex = "Keywords: *\n"
        old_uregex = "(\W*|)www.*.*"


        eol = "\n"
        eolc = 0

        title = ""
        watchd = 0
        Wflag = 0

        ac = ""
        ref = ""

        nt = ""
        cr = ""
        ds = ""
        cn = ""

        try:
            ficher = open(Fname, "r", errors='ignore')
        except:
            return
        abst = ""
        auth = ""
        refs = ""
        kwind = ""
        for line in ficher:
            l = line[:-1] if len(line)>1 else line
            s = ''.join([i for i in l if ord(i)<127])
            st = ''.join([i for i in l if i in _ASCII_TEXT]).lstrip()
            if l in SKIP:
                continue
            if watchd>0 and title=="":
                inT = True
            if inK and line != eol:
                kwind += line[:-1]
                kwind += " "
            else:
                inK = False
            if re.search(kireg, line, re.IGNORECASE) and Wflag == 1:
                inK = True
                inW = False
                Wflag = 1
                #print " {} ".format(line[:-1])
                continue
            #if inT and re.search(nreg, line) and Wflag == 0:
            #    title = ""
            #    watchd = 0
                #continue
            try:
                if Wflag == 0 and not False in [(i[0].isupper() or i in REMOV_TITLE) for i in st.split(" ")]:
                    #print(" {} {} ".format([(i[0].isupper() or i in REMOV_TITLE) for i in l.split(" ")], line[:-1]))
                    inT = False
                    inW = False
            except:
                # print(l+"\n")
                pass
            if Wflag == 0 and re.search(uregex, line, re.IGNORECASE):
                inT = False
                title = ""
                watchd = 0
            if inT:
                # print " {} {} ".format([(i[0].isupper() or i in REMOV_TITLE) for i in l.split(" ")], line[:-1])
                title += line[:-1]
                title += " "
            if Wflag == 0 and re.search(regex, line, re.IGNORECASE):
                line = line[len(regex)-2:]
                inW = True
                Wflag = 1
            if l in INTREND:
                inBC = 0
                inI = False
                inCo = True
                inB = ''
            if line == eol or re.search(nreg, line):
                line = ""
                inW = False
                intT = False
                if inBC != 0 and inB != 0:
                    inBC -= 1
                elif inBC == 0 and len(nt.lstrip())<=3:
                    inBC = 2
                    inB = 'i'
                elif inBC == 0 and inB != 0:
                    inB = 0
                eolc += 1
            else:
                eolc = 0
            if inR:
                if eolc >= 2:
                    inR = False
                refs += line[:-1]
                refs += " "
            if re.search(rregex, line, re.IGNORECASE) or (len(line)>len(rfregex) and line[1:]==rfregex):
                inR = True
            if inI:
                if l in INTREND:
                    inI = False
                    continue
                else:
                    nt += l
                    l += " "
            if inBC == 0 and inB != 0:
                inB = 0
            if st in REFS:
                inCo = False
                inB = 'r'
                inBC = 12
                continue
            if s in ACK:
                inB = 'a'
                inBC = 12
                continue
            if st in DISC:
                inCo = False
                inB = 'd'
                inBC = 8
                # print l, st
                continue
            if True in [l.startswith(i) for i in CORPS]:
                inBC = 0
                inC = True
            if st in INTR:
                inI = True
                inB = 'i'
                inBC = -1
                continue
            if st in CONCL:
                inCo = False
                inB = 'c'
                inBC = 16
                continue
            if inB != 0 and inBC != 0:
                if inB == 'r':
                    ref += l
                    ref += " "
                elif inB == 'a':
                    ac += l
                    ac += " "
                elif inB == 'd':
                    ds += l
                    ds += " "
                elif inB == 'i':
                    #nt += l
                    #nt += " "
                    pass
                elif inB == 'c':
                    if st in ACK or s in CONCL_END:
                        inBC = 0
                        continue
                    else:
                        cn += l
                        cn += " "
                else:
                    pass
                    #pass
            if inW:
                abst += line[:-1]
                abst += ' '
            if not inW and not inT and Wflag == 0 and not re.search(uregex, line, re.IGNORECASE):
                if not True in [st.startswith(i) for i in AUTH_END]:
                    auth += line[:-1]
                    auth += ' '
                else:
                    inT = False
                    inW = True
                    Wflag = 1
                    abst += line[:-1]
                    abst += ' '
                    #print(st)
                #print(line[:-1])
            if inCo:
                cr += l
                cr += ' '
            watchd+=1
        """
            <article>
                <preambule>{TITLE_ORIGIN}</preambule>
                <titre>{TITLE}</titre>
                <auteur>{AUT}</auteur>
                <abstract>{ABSTR}</abstract>
                <biblio>{BIBILO}</biblio>
            </article>
        """
        fFname = Fname[:-4]
        outFname = '{}-{}.{}'.format(fFname, _DESC, _EOUT)
        Fsplt = outFname.split('/')
        Out = '{}/{}/{}'.format('/'.join(Fsplt[:-1]), outf, ''.join(Fsplt[-1:]))
        f = open(Out, "w+")

        # print(Out)

        # Sanitize spaces
        title = ' '.join(title.split())
        abst = ' '.join(abst.split())
        auth = ' '.join(auth.split())
        auth = auth.replace(" , ", ", ") # Oxford comma, please.
        auth = auth.replace(" : ", ": ").replace(" ; ", "; ")
        if len(refs) <=1 and len(ref)>1: refs = ref;
        refs = ' '.join(refs.split())

        if(self.XML):
            """ Escaping like a -BOSS-"""
            f.write("<{}>\n".format(self.XML_TAGS['_ARTICLE']))
            if self.DO['_PREAMBULE']: f.write("\t<{0}>{1}</{0}>\n".format(self.XML_TAGS['_PREAMBULE'], Fname.split('/')[-1][:-len(_EOUT)-1]))
            if self.DO['_TITRE']: f.write("\t<{0}>{1}</{0}>\n".format(self.XML_TAGS['_TITRE'], self.html_escape(title)))
            if self.DO['_AUTEUR']: f.write("\t<{0}>{1}</{0}>\n".format(self.XML_TAGS['_AUTEUR'], self.html_escape(auth)))
            if self.DO['_ABSTRACT']: f.write("\t<{0}>{1}</{0}>\n".format(self.XML_TAGS['_ABSTRACT'], self.html_escape(abst)))
            if self.DO['_BIBLIO']: f.write("\t<{0}>{1}</{0}>\n".format(self.XML_TAGS['_BIBLIO'], self.html_escape(refs)))
            # PLUS
            if self.DO['_INTR']: f.write("\t<{0}>{1}</{0}>\n".format(self.XML_TAGS['_INTR'], self.html_escape(nt)))
            if self.DO['_CORP']: f.write("\t<{0}>{1}</{0}>\n".format(self.XML_TAGS['_CORP'], self.sanitize_body(self.html_escape(cr))))
            if self.DO['_DISC']: f.write("\t<{0}>{1}</{0}>\n".format(self.XML_TAGS['_DISC'], self.html_escape(ds)))
            if self.DO['_CONCL']: f.write("\t<{0}>{1}</{0}>\n".format(self.XML_TAGS['_CONCL'], self.html_escape(cn)))
            f.write("</{}>".format(self.XML_TAGS['_ARTICLE']))
        else :
            """ OneLine Compress """
            title = ' '.join(title.split())
            auth = ' '.join(auth.split())
            abst = ' '.join(abst.split())
            refs = ' '.join(refs.split())
            nt = ' '.join(nt.split())
            cr = ' '.join(self.sanitize_body(cr).split())
            ds = ' '.join(ds.split())
            cn = ' '.join(cn.split())
            if self.DO['_HEADER']: f.write("{}".format(self.TXT_TAGS['_HEADER']))
            if self.DO['_PREAMBULE']: f.write("{}{}".format(self.TXT_TAGS['_PREAMBULE'], Fname.split('/')[-1][:-len(_EOUT)-1]))
            if self.DO['_TITRE']: f.write("{}{}".format(self.TXT_TAGS['_TITRE'], title))
            if self.DO['_AUTEUR']: f.write("{}{}".format(self.TXT_TAGS['_AUTEUR'], auth))
            if self.DO['_ABSTRACT']: f.write("{}{}".format(self.TXT_TAGS['_ABSTRACT'], abst))
            if self.DO['_BIBLIO']: f.write("{}{}".format(self.TXT_TAGS['_BIBLIO'], refs))

            if self.DO['_INTR']: f.write("{}{}".format(self.TXT_TAGS['_INTR'], nt))
            if self.DO['_CORP']: f.write("{}{}".format(self.TXT_TAGS['_CORP'], cr))
            if self.DO['_DISC']: f.write("{}{}".format(self.TXT_TAGS['_DISC'], ds))
            if self.DO['_CONCL']: f.write("{}{}".format(self.TXT_TAGS['_CONCL'], cn))
            #f.write("{}\n{}\n{}".format(Fname.split('/')[-1], title, abst))
        # print(abst[:_MAX_LEN])
        # print("\n")
        # print(title[:_MAX_LEN])
        #
        return Out

    def parse(self, fname):
        return self.name + fname
