import os.path
import json
with open('lines.json', 'w') as lines:
    line = {}
    with open('entity.json', 'r') as f:
        data = json.load(f)
        for entity in data:
            # if os.path.isfile(entity['Image']):
            line[entity['Name']] = entity['Lines']
            print('Checking {},'.format(entity['Name']))
        lines.write(json.dumps(line))
