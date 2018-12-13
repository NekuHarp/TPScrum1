import re
import sys
import glob
import os
import subprocess
import argparse

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

_CFLAG = ['t', 'x']
_SFLAG = '-'
_FLAGS = [_SFLAG+i for i in _CFLAG]

_MAX_LEN = 80

XML = False
Text = False

def parser(Fname):
    inW = False
    inT = True

    regex = "Abstract.*\n"
    eol = "\n"

    title = ""
    watchd = 0

    ficher = open(Fname, "r")
    abst = ""
    for line in ficher:
        if watchd>1 and title=="":
            inT = True
        if not False in [i[0].isupper() for i in line.split(" ")]:
            inT = False
        if inT:
            title += line[:-1]
            title += " "
        if re.search(regex, line):
            inW = True
        if line == eol:
            inW = False
            intT = False
        if inW:
            abst += line[:-1]
            abst += ' '
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
    Out = '{}/{}/{}'.format('/'.join(Fsplt[:-1]), outF, ''.join(Fsplt[-1:]))
    f = open(Out, "w+")

    if(XML):
        f.write("<{}>".format(_ARTICLE))
        f.write("<{0}>{1}</{0}>".format(_PREAMBULE, Fname.split('/')[-1]))
        f.write("<{0}>{1}</{0}>".format(_TITRE, title))
        f.write("<{0}>{1}</{0}>".format(_AUTEUR, "AUTEUR"))
        f.write("<{0}>{1}</{0}>".format(_ABSTRACT, abst))
        f.write("<{0}>{1}</{0}>".format(_BIBLIO, "BIBLIO"))
        f.write("</{}>".format(_ARTICLE))
    else :
        f.write("{}\n{}\n{}".format(Fname.split('/')[-1], title, abst))
    print(abst[:_MAX_LEN])
    print("\n")
    print(title[:_MAX_LEN])



def getFiles(wd):
    gl = glob.glob('{}/*.{}'.format(wd, _EXT))
    outD = '{}/{}'.format(wd, outF)
    if not os.path.exists(outD):
        os.makedirs(outD)
    for g in gl:
        Fname = '{}.{}'.format(g[:-4], _TXT)
        p = subprocess.Popen([_APP , g , Fname])
        p.wait()

        parser(Fname)


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
    print(args)
    XML = args.xml
    if(XML):
        _EOUT = 'xml'
    Text = args.text

    arg = sys.argv
    print(arg)
    print(_FLAGS)

    getFiles(args.folder)