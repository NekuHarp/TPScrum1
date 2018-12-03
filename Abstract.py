import re
import sys
import glob
import subprocess


def parser(fname):
    inW = False
    inT = True

    regex = "Abstract.*\n"
    eol = "\n"

    title = ""
    watchd = 0

    ficher = open(fname, "r")
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
    print(abst[:80])
    print("\n")
    print(title[:80])

    ffname = fname[:-4]
    outFname = '{0}-desc.txt'.format(ffname)
    f = open(outFname, "w")
    f.write("{0}\n{1}\n{2}".format(fname.split('/')[-1], title, abst))


def getFiles():
    gl = glob.glob('./*.pdf')

    for g in gl:
        fname = '{0}.txt'.format(g[:-4])
        p = subprocess.Popen(['pdftotext' , g , fname])
        p.wait()

        parser(fname)


if __name__ == '__main__':
    getFiles()
