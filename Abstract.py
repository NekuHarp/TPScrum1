import re
import sys
import glob
import subprocess

inW = False

regex = "Abstract.*\n"
eol = "\n"

gl = glob.glob('./*.pdf')


for g in gl:
    print("\n")
    fname = '{0}.txt'.format(g[:-4])
    print(g)
    print(fname)
    p = subprocess.Popen(['pdftotext' , g , fname])
    p.wait()

    file = open(fname, "r")
    abst = ""

    for line in file:
        if re.search(regex, line):
            inW = True
        if line == eol:
            inW = False
        if inW:
            abst += ' '
            abst += line[:-1]
    print(abst)
