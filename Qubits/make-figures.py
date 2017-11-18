#!/usr/bin/python

filenames = [
    'single_circuit_with_drive',
    'coupled_circuits_capacitive',
    'coupled_circuits_inductive',
]


command = ''
for name in filenames:
    command += "echo {}.svg --export-pdf={}.pdf;\n".format(name, name)
command = "({}) |\nDISPLAY= inkscape --shell".format(command)


import os
os.system(command)

