import subprocess

amazon = ['pygame', 'pyinstaller']

for package in amazon:
    subprocess.call(['py', '-m', 'pip', 'install', package])

print('Spawning new python window')
subprocess.call(['py', './main.py'])
# subprocess.call(['pyinstaller', '--onefile', 'main.py'])
