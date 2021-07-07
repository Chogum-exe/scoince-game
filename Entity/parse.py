import json
with open('entity.json', 'r') as f:
    data = json.load(f)
    for entity in data['Entity']:
