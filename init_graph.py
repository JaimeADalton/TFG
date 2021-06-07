#!/usr/bin/env python
import os
import time

os.system('bash TimeDuData.sh')
time.sleep(60)
os.system('python join_data_files.py')
time.sleep(60)
os.system('python clean_data.py')
time.sleep(60)

with os.scandir('.') as directorios:
    directorios = [directorio.name for directorio in directorios if directorio.is_dir()]

if 'RawData' in directorios:
    directorios.pop(directorios.index('RawData'))
if 'compare_graphs' in directorios:
    directorios.pop(directorios.index('compare_graphs'))

for dirs in directorios:
    os.system('python graphs.py ' + str(dirs))

time.sleep(5)
os.system('python compare_graphs.py')
