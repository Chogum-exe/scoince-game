import subprocess
import os
import shutil
amazon = ['pygame', 'pyinstaller', 'shutil']
for package in amazon:
    if os.name == 'nt':
        subprocess.call(['py', '-m', 'pip', 'install', package])
    else:
        subprocess.call(['python', '-m', 'pip', 'install', package])
#
# print('Game Builder: Spawning new python window')
# subprocess.call(['python', 'main.py'])

print(os.name)
if os.name == 'nt':
    APP_PATH = "C:/Somthing/Somthing/Soemthing"
if os.name == 'posix':
    APP_PATH = "/Applications"

destination = shutil.move('/Users/ryan/Documents/GitHub/Host/scoince-game', APP_PATH, copy_function = shutil.copytree)
# os.getcwd()
print('Game Builder: moved to: ' + destination)


# subprocess.call(['pyinstaller', '--onefile', 'main.py'])
