#!/usr/bin/python3
import dis
import marshal

with open('/tmp/hidden_4.pyc', 'rb') as fichier:
    code = marshal.load(fichier)

noms = set()
for instruction in dis.get_instructions(code):
    if instruction.opname == 'STORE_NAME' and not instruction.argrepr.startswith('__'):
        noms.add(instruction.argrepr)

for nom in sorted(noms):
    print(nom)
