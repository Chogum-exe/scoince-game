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

print('Game Builder: Detected os by name of: ' + os.name)
if os.name == 'nt':
    APP_PATH = "C:\Program"
if os.name == 'posix':
    APP_PATH = "/Applications"

print(os.getcwd())
destination = shutil.move(os.getcwd(), APP_PATH, copy_function = shutil.copytree)
# os.getcwd()
print('Game Builder: moved to: ' + str(destination))


# subprocess.call(['pyinstaller', '--onefile', 'main.py'])
