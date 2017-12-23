#!/usr/bin/python

filenames = [
    'basic_circuit',
    'reflection_circuit',
    'lollipop',
    'S21_circle'
]

import os

command = ''
for name in filenames:
    command += "echo {}/{}.svg --export-pdf={}/{}.pdf;\n".format(
            os.getcwd(), name, os.getcwd(), name)
command = "({}) |\nDISPLAY= inkscape --shell".format(command)


os.system(command)

