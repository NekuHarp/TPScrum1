import inquirer
import glob
import os

_EXT = 'pdf'

wd = './dossier'
l = len(wd)+1
gl = glob.glob('{}/*.{}'.format(wd, _EXT))
Hmap = {}
for i in gl:
    Hmap[i[l:].replace('_',' ')]=i
ch = [i for i in Hmap]

questions = [
  inquirer.Checkbox('PDF',
                    message="Which do you want to convert?",
                    choices=ch,
                    ),
]
answers = inquirer.prompt(questions)

print [Hmap[i] for i in answers['PDF']]
