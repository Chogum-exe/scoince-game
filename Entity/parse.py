import os.path
import json


f1 = open('lines.json', 'w')
lines = {}
f2 = open('position.json', 'w')
pos = {}

with open('entity.json', 'r') as f:
    data = json.load(f)
    for entity in data:
        print('Checking {},'.format(entity['Name']))
        lines[entity['Name']] = entity['Lines']
        pos[entity['Name']] = entity['Location']
    f1.write(json.dumps(lines, indent=4))
    f2.write(json.dumps(pos, indent=4))
