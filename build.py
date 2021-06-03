import subprocess

amazon = ['pygame', 'pyinstaller']

for package in amazon:
    subprocess.call(['pip', 'install', package])

print('Spawning new python window')
subprocess.call(['python', 'main.py'])
# subprocess.call(['pyinstaller', '--onefile', 'main.py'])
