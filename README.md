# TPScrum1

## Imported libraries

* `re`: regular expressions
* `sys`: systel-specific parameters and functions
* `glob`: Unix-style pathname pattern expransion
* `os`: miscellaneous operating system interfaces
* `subprocess`: subprocess management
* `argparse`: parser for command-line options

## Usage

* Synopsis: `python abstract.py OPTION DIRECTORY`
* Available options:
    - `-t`: output in plain text format
    - `-x`: output in XML format
* Output:
    - PDFtoText files will be created in given directory
    - a new directory (called *out*) will be created 

## How it works

Our program uses PDFtoText to convert PDF files (found in a given directory) to plain text files, and output them in the same directory. Then it creates a new folder in the given directory, called *out*, which contains our parser's output.