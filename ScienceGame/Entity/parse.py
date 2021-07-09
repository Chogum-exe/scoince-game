from os import path
import json

with open('entity.json', 'r') as f:
    data = json.load(f)
    for entity in data:
        print(entity['Image'])
        if os.path.isfile("Image"):
            pass
        else:
            print('ohno')
            e = 'a'
            print(f"{{{e}}}")

            e = 'a'
print(f"{{{e}}}")
