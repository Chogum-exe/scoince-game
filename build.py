import subprocess
import os
amazon = ['pygame', 'pyinstaller', 'shutil']
for package in amazon:
    subprocess.call(['python', '-m', 'pip', 'install', package])

print('Spawning new python window')
# subprocess.call(['python', 'main.py'])

print(os.name)
if os.name == 'nt':
    APP_PATH = "C:/Somthing/Somthing/Soemthing"
if os.name = 'posix'
    APP_PATH = "Path/Path/thing"

destination = shutil.move(os.cwd, APP_PATH, copy_function = shutil.copytree)
print('moved to: ' + destination)
# if os.name

# subprocess.call(['pyinstaller', '--onefile', 'main.py'])

