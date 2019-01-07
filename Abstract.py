# -*- coding: utf-8 -*-
import re
import sys
import glob
import os
import subprocess
import argparse
import time

APP_NAME = 'PDF Parser 1.1'
HELP_MSG = ['Creating output folder . . .','','','Tasks complete !']

outF = 'out'
_APP = 'pdftotext'
_EXT = 'pdf'
_TXT = 'txt'
_EOUT = 'txt'
_DESC = 'desc'

_ARTICLE = 'article'
_PREAMBULE = 'preambule'
_TITRE = 'titre'
_AUTEUR = 'auteur'
_ABSTRACT = 'abstract'
_BIBLIO = 'biblio'

_ACK = 'acknowledgements'
_REFS = 'references'

_INTR = 'introduction'
_CORP = 'corps'
_DISC = 'discussion'
_CONCL = 'conclusion'

_CFLAG = ['t', 'x']
_SFLAG = '-'
_FLAGS = [_SFLAG+i for i in _CFLAG]

SKIP = ['IEEE TRANSACTIONS ON SPEECH AND AUDIO PROCESSING, VOL. 12, NO. 4, JULY 2004', '401']

REMOV_TITLE = [',', 'and', 'a,*,', 'a,', 'b,1', 'of']
IGNORE_ME = ['in', 'and', 'for']

DISC = ['Discussion']
ACK = ['Acknowledgements', 'ACKNOWLEDGMENT']
REFS = ['References', 'REFERENCES']
CONCL = ['Conclusion', 'Conclusions', 'CONCLUSIONS AND FURTHER WORK', 'Conclusions and further work', 'Conclusions and future work', 'Conclusion and Future Work', 'IV CONCLUSION']
INTR = ['Introduction', 'I INTRODUCTION', 'Introduction', 'INTRODUCTION', 'Introduction']

CORPS = ['2.','2','II.']

_MAX_LEN = 80

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

        self.checkDir()

    def checkDir(self):
        if not os.path.exists(self.outD):
            os.makedirs(self.outD)

    def _update(self):
        self.outD = '{}/{}'.format(self.wd, self.outF)
        self.checkDir()

    def setWD(self, wd):
        if os.path.exists(wd):
            self.wd = wd
            self._update()
            return True
        else:
            return False

    def setOut(self, outf):
        self.outF = outf
        if not os.path.exists(self.outF):
            os.makedirs(self.outF)
        self._update()
        return True

    def listDir(self, wd=''):
        if wd == '':
            wd = self.wd
        if os.path.exists(wd):
            gl = glob.glob('{}/*.{}'.format(wd, "pdf"))
            gl = [g.replace('\\','/') for g in gl]
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
        r = parser(Fname, xml=True, outf=self.outF)
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
        r = parser(Fname, xml=False, outf=self.outF)
        if q!='': q.put(r)
        return r

    def fromPDFtoXML(self, fname, q=''):
        Fname = '{}.{}'.format(fname[:-4], _TXT)
        p = subprocess.Popen([_APP , fname , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
        p.wait()
        r = parser(Fname, xml=True, outf=self.outF)
        if q!='': q.put(r)
        return r

    def fromPDFtoTXT(self, fname, q=''):
        Fname = '{}.{}'.format(fname[:-4], _TXT)
        p = subprocess.Popen([_APP , fname , Fname], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
        p.wait()
        r = parser(Fname, xml=False, outf=self.outF)
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

    ficher = open(Fname, "r")
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
            if Wflag == 0 and not False in [(i[0].isupper() or i in REMOV_TITLE) for i in l.split(" ")]:
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
            else:
                inBC = 0
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
        if inBC == 0 and inB != 0:
            inB = 0
        if st in REFS:
            inB = 'r'
            inBC = 12
            continue
        if s in ACK:
            inB = 'a'
            inBC = 12
            continue
        if st in DISC:
            inB = 'd'
            inBC = 4
            # print l, st
            continue
        if True in [l.startswith(i) for i in CORPS]:
            inBC = 0
            inC = True
        if st in INTR:
            inB = 'i'
            inBC = 16
            continue
        if st in CONCL:
            inB = 'c'
            inBC = 2
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
                nt += l
                nt += " "
            elif inB == 'c':
                cn += l
                cn += " "
            else:
                pass
                #pass
        if inW:
            abst += line[:-1]
            abst += ' '
        if not inW and not inT and Wflag == 0 and not re.search(uregex, line, re.IGNORECASE):
            auth += line[:-1]
            auth += ' '
            #print(line[:-1])
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
        f.write("<{}>\n".format(_ARTICLE))
        f.write("\t<{0}>{1}</{0}>\n".format(_PREAMBULE, Fname.split('/')[-1][:-len(_EOUT)-1]))
        f.write("\t<{0}>{1}</{0}>\n".format(_TITRE, title))
        f.write("\t<{0}>{1}</{0}>\n".format(_AUTEUR, auth))
        f.write("\t<{0}>{1}</{0}>\n".format(_ABSTRACT, abst))
        f.write("\t<{0}>{1}</{0}>\n".format(_BIBLIO, refs))
        # PLUS
        f.write("\t<{0}>{1}</{0}>\n".format(_INTR, nt))
        f.write("\t<{0}>{1}</{0}>\n".format(_CORP, cr))
        f.write("\t<{0}>{1}</{0}>\n".format(_DISC, ds))
        f.write("\t<{0}>{1}</{0}>\n".format(_CONCL, cn))
        f.write("</{}>".format(_ARTICLE))
    else :
        f.write("{}\n{}\n{}".format(Fname.split('/')[-1], title, abst))
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
