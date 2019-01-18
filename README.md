# TPScrum1

## Imported libraries

* `re`: regular expressions
* `sys`: systel-specific parameters and functions
* `glob`: Unix-style pathname pattern expransion
* `os`: miscellaneous operating system interfaces
* `subprocess`: subprocess management
* `argparse`: parser for command-line options
* `cefpython3`: User Interface
* `Pickle`: settings save & load
* `threading`: non-blocking run
* `queue`: data queueing

## Usage

To install the parser run:

`python setup.py install`

and then simply use the two launchers from `bin/`

~~* Synopsis: `python abstract.py OPTION DIRECTORY`~~ (Deprecapted. Please install it properly)

### CLI Usage (pdfparser)

* Available options:
    - `-t`: output in plain text format
    - `-x`: output in XML format
    - `./dossier`: input folder
* Output:
    - PDFtoText files will be created in given directory
    - a new directory (called *out*) will be created 

### GUI Usage (pdfparser-gui)

* Change input / output folder:
    - go on the `menu` , into `core` 
    - change `Search path` for the input and `Output folder` for the output files

* Use keys for a faster use:
    - Open the menu with the `,` key
    - Toggle XML / TXT with the `x` key
    - Launch conversion or save settings with the `Enter` key
    - Learn more in the `menu` , under `Keybind`

* Visualize the output:
    - go on the `menu` , into `Structures` 
    - Scroll a bit, file synthaxes are here !

> I have a weird `No Files Found.` message

Check both your input and the console at the bottom. Directory should be empty or invalid. 

## How it works

Our program uses PDFtoText to convert PDF files (found in a given directory) to plain text files, and output them in the same directory. Then it creates a new folder in the given directory, called *out*, which contains our parser's output.
