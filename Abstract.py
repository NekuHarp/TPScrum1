import re
import sys

inW = False

regex = "Abstract.*\n"
eol = "\n"

abst = ""

file = open(sys.argv[1], "r")

for line in file:
    if re.search(regex, line):
        inW = True
    if line == eol:
        inW = False
    if inW:
        abst += line[:-1]
print(abst)
