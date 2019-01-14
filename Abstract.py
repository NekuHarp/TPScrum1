# -*- coding: utf-8 -*-
import re
import sys
import glob
import os
import subprocess
import argparse
import time
import pickle

TEST = 1

APP_NAME = 'PDF Parser 1.1'
VERSION = '1.0.1 e r0'
HELP_MSG = ['Creating output folder . . .','','','Tasks complete !']

outF = 'out'
_APP = 'pdftotext'
_EXT = 'pdf'
_TXT = 'txt'
_EOUT = 'txt'
_DESC = 'desc'

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

XML = False
Text = False

_COUNT_SZ = 20
COUNT = 0

class Parser:
    def __init__(self, wd='./dossier', outf=outF):
        self.name = APP_NAME
        self.wd = wd
        self.outF = outf
        self.outD = '{}/{}'.format(self.wd, self.outF)

        self.loadConfig()
        self.checkDir()

    def checkDir(self):
        if not os.path.exists(self.outD):
            os.makedirs(self.outD)

    def getVersion(self):
        return VERSION

    def getXMLTags(self):
        return _XML_TAGS

    def getXMLTag(self, val):
        return '' if not val in _XML_TAGS else _XML_TAGS[val]

    def setXMLTag(self, key, val):
        if key in _XML_TAGS:
            _XML_TAGS[key] = val
            return True
        return False

    def getTXTTags(self):
        return _TXT_TAGS

    def getTXTTag(self, val):
        return '' if not val in _TXT_TAGS else _TXT_TAGS[val]

    def setTXTTag(self, key, val):
        if key in _TXT_TAGS:
            _TXT_TAGS[key] = val
            return True
        return False

    def getDoTags(self):
        return _DO

    def getDoTag(self, val):
        return '' if not val in _DO else _DO[val]

    def setDoTag(self, key, val):
        if key in _DO:
            _DO[key] = val
            return True
        return False

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

    def listDir(self, wd=''):
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
            r = parser(Fname, xml=True, outf=self.outF)
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
            r = parser(Fname, xml=False, outf=self.outF)
        except:
            r = ''
        if q!='': q.put(r)
        return r

    def fromPDFtoXML(self, fname, q=''):
        Fname = '{}.{}'.format(fname[:-4], _TXT)
        if not checkPDF(fname): return ''
        p = subprocess.Popen([_APP , fname , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
        p.wait()
        try:
            r = parser(Fname, xml=True, outf=self.outF)
        except:
            r = ''
        if q!='': q.put(r)
        return r

    def fromPDFtoTXT(self, fname, q=''):
        Fname = '{}.{}'.format(fname[:-4], _TXT)
        if not checkPDF(fname): return ''
        p = subprocess.Popen([_APP , fname , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
        p.wait()
        try:
            r = parser(Fname, xml=False, outf=self.outF)
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

    def saveConfig(self, fname="config.pak"):
        _out = open(fname, 'wb')
        pickle.dump(_DO, _out)
        pickle.dump(_XML_TAGS, _out, -1)
        pickle.dump(_TXT_TAGS, _out, -1)
        pickle.dump(self.wd, _out, -1)
        pickle.dump(self.outF, _out, -1)
        _out.close()

    def loadConfig(self, fname="config.pak"):
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

def html_escape(raw):
    return "".join(HTML_ESCAPE_TABLE.get(c,c) for c in raw)

def sanitize_body(raw):
    try:
        return ' '.join(("\n".join([i for i in raw.split("\n") if len(i)>4 and not (len(i) == len([j for j in i if j in _DIGITS]))])).split(' '))
    except:
        return raw

# print '[100m {} [49m\n'.format(APP_NAME)
# for i in range(11):
#     time.sleep(0.2)
#     progress(i, 10, 20)
#     status('{}'.format(i))

def parser(Fname, xml=XML, outf=outF):
    inW = False
    inR = False
    inT = True
    inR = False
    inK = False
    inC = True
    inI = False

    inCo = False

    if(xml):
        XML = True
        _EOUT = 'xml'
    else:
        XML = False
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

    if(XML):
        """ Escaping like a -BOSS-"""
        f.write("<{}>\n".format(_XML_TAGS['_ARTICLE']))
        if _DO['_PREAMBULE']: f.write("\t<{0}>{1}</{0}>\n".format(_XML_TAGS['_PREAMBULE'], Fname.split('/')[-1][:-len(_EOUT)-1]))
        if _DO['_TITRE']: f.write("\t<{0}>{1}</{0}>\n".format(_XML_TAGS['_TITRE'], html_escape(title)))
        if _DO['_AUTEUR']: f.write("\t<{0}>{1}</{0}>\n".format(_XML_TAGS['_AUTEUR'], html_escape(auth)))
        if _DO['_ABSTRACT']: f.write("\t<{0}>{1}</{0}>\n".format(_XML_TAGS['_ABSTRACT'], html_escape(abst)))
        if _DO['_BIBLIO']: f.write("\t<{0}>{1}</{0}>\n".format(_XML_TAGS['_BIBLIO'], html_escape(refs)))
        # PLUS
        if _DO['_INTR']: f.write("\t<{0}>{1}</{0}>\n".format(_XML_TAGS['_INTR'], html_escape(nt)))
        if _DO['_CORP']: f.write("\t<{0}>{1}</{0}>\n".format(_XML_TAGS['_CORP'], sanitize_body(html_escape(cr))))
        if _DO['_DISC']: f.write("\t<{0}>{1}</{0}>\n".format(_XML_TAGS['_DISC'], html_escape(ds)))
        if _DO['_CONCL']: f.write("\t<{0}>{1}</{0}>\n".format(_XML_TAGS['_CONCL'], html_escape(cn)))
        f.write("</{}>".format(_XML_TAGS['_ARTICLE']))
    else :
        """ OneLine Compress """
        title = ' '.join(title.split())
        auth = ' '.join(auth.split())
        abst = ' '.join(abst.split())
        refs = ' '.join(refs.split())
        nt = ' '.join(nt.split())
        cr = ' '.join(sanitize_body(cr).split())
        ds = ' '.join(ds.split())
        cn = ' '.join(cn.split())
        if _DO['_HEADER']: f.write("{}".format(_TXT_TAGS['_HEADER']))
        if _DO['_PREAMBULE']: f.write("{}{}".format(_TXT_TAGS['_PREAMBULE'], Fname.split('/')[-1][:-len(_EOUT)-1]))
        if _DO['_TITRE']: f.write("{}{}".format(_TXT_TAGS['_TITRE'], title))
        if _DO['_AUTEUR']: f.write("{}{}".format(_TXT_TAGS['_AUTEUR'], auth))
        if _DO['_ABSTRACT']: f.write("{}{}".format(_TXT_TAGS['_ABSTRACT'], abst))
        if _DO['_BIBLIO']: f.write("{}{}".format(_TXT_TAGS['_BIBLIO'], refs))

        if _DO['_INTR']: f.write("{}{}".format(_TXT_TAGS['_INTR'], nt))
        if _DO['_CORP']: f.write("{}{}".format(_TXT_TAGS['_CORP'], cr))
        if _DO['_DISC']: f.write("{}{}".format(_TXT_TAGS['_DISC'], ds))
        if _DO['_CONCL']: f.write("{}{}".format(_TXT_TAGS['_CONCL'], cn))
        #f.write("{}\n{}\n{}".format(Fname.split('/')[-1], title, abst))
    # print(abst[:_MAX_LEN])
    # print("\n")
    # print(title[:_MAX_LEN])
    #
    return Out



def getFiles(wd, xml=XML):
    gl = glob.glob('{}/*.{}'.format(wd, _EXT))
    outD = '{}/{}'.format(wd, outF)

    print('[100m {} [49m\n'.format(APP_NAME))
    COUNT = len(gl)
    pos = 0
    gl = [g.replace('\\','/') for g in gl]

    if not os.path.exists(outD):
        os.makedirs(outD)
        progress(pos, COUNT, _COUNT_SZ)
        status('{}'.format(HELP_MSG[0]))
    for g in gl:
        pos += 1
        progress(pos, COUNT, _COUNT_SZ)
        fnam = os.path.basename(g)
        if len(fnam)+4>_MAX_LEN: fnam = fnam[:(_MAX_LEN-4-3)]+"..."
        else: fnam += ' '*(_MAX_LEN-4-len(fnam))
        status(' > {}'.format(fnam))

        Fname = '{}.{}'.format(g[:-4], _TXT)
        p = subprocess.Popen([_APP , g , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
        p.wait()
        parser(Fname, xml)
    print('\n'+HELP_MSG[3])

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='scientific articles parser')
    p.add_argument("folder",
                    help="input file with two matrices", metavar="./documents",
                    type=lambda x: x if os.path.isdir(x) else '.')
    p.add_argument('-t', '--text', action='store_true',
                        help='Save as text')
    p.add_argument('-x', '--xml', action='store_true',
                        help='Save as XML')

    args = p.parse_args()
    # print(args)
    XML = args.xml
    if(XML):
        print('XML')
        _EOUT = 'xml'
    Text = args.text

    arg = sys.argv
    # print(arg)
    # print(_FLAGS)

    getFiles(args.folder, XML)
