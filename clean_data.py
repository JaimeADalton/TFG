#!/usr/bin/env python
import os
dir_files=[]
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            dir_files.append(os.path.join(root, file))

for file in dir_files:
    if file not in ['./RawData/data.txt','./counter.txt']:
        f = open(file,'r')
        texto = f.read().replace(' ','')
        f.close()
        f = open(file , 'w')
        f.write(texto)
        f.close()
