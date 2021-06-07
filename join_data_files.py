#!/usr/bin/env python
import subprocess
import os
import csv


'''
Algoritmo que devuelve el ratio 1 - (tamaño_final / tamaño_original) de todos los estudios
'''
f = open('./ratio_results.txt' , 'w')
results=[]
for estudio in range(1,9):
    for test in range(1,71):
        num_estudio = estudio
        if num_estudio == 1 or num_estudio == 2 or num_estudio == 3:
            real_size = 26214400
        if num_estudio == 4:
            real_size = 15549809
        if num_estudio == 5:
            real_size = 26214400
        if num_estudio == 6:
            real_size = 26444800
        if num_estudio == 7:
            real_size = 36561408
        if num_estudio == 8:
            real_size = 39469568
        files_dir=subprocess.check_output('find Estudio_' + str(estudio) + ' -type d -iname '+ str(test), shell=True).decode("utf-8").strip()
        result=int(subprocess.check_output(('cat ' + str(files_dir) + '/*' + str(test) + '.du | cut -d R -f 1'), shell=True).decode("utf-8").strip())
        f.write(str(1 - (result / real_size)) + ',' + str(estudio) + ',' + str(test) + '\n')
f.close()

'''
Algoritmo que agrupa todos los valores de tiempo de ejecucion de cada algoritmo
'''
f = open('./time_results.txt' , 'w')
results=[]
for estudio in range(1,9):
    for test in range(1,71):
        files_dir=subprocess.check_output('find Estudio_' + str(estudio) + ' -type d -iname '+ str(test), shell=True).decode("utf-8").strip()
        result=subprocess.check_output(('cat ' + str(files_dir) + '/*' + str(test) + ".time | awk '{print $1}' | head -n1 | sed 's/user//'"), shell=True).decode("utf-8").strip()
        f.write(result + ',' + str(estudio) + ',' + str(test) + '\n')
f.close()

'''
Algoritmo que agrupa el uso de CPU
'''

f = open('./cpu_results.txt' , 'w')
results=[]
for estudio in range(1,9):
    for test in range(1,71):
        files_dir=subprocess.check_output('find Estudio_' + str(estudio) + ' -type d -iname '+ str(test), shell=True).decode("utf-8").strip()
        result=subprocess.check_output(('cat ' + str(files_dir) + '/*' + str(test) + ".time | awk '{print $4}' | head -n1 | sed 's/\%CPU//'"), shell=True).decode("utf-8").strip()
        f.write(result + ',' + str(estudio) + ',' + str(test) + '\n')
f.close()


f = open('ecomp_results.txt', 'w')
data = open('TimeDuData.txt', 'r')
for line in csv.reader(data):
    estudio = int(line[0])
    num_estudio = estudio
    if num_estudio == 1 or num_estudio == 2 or num_estudio == 3:
        real_size = 26214400
    if num_estudio == 4:
        real_size = 15549809
    if num_estudio == 5:
        real_size = 26214400
    if num_estudio == 6:
        real_size = 26444800
    if num_estudio == 7:
        real_size = 36561408
    if num_estudio == 8:
        real_size = 39469568
    program_name = line[1]
    iteration = int(line[2])
    Bytes = int(line[3])
    user = float(line[4])
    system = float(line[5])
    CPU = int(line[7])
    ecomp = (1 - (Bytes / real_size)) / ( user + system )
    f.write(str(estudio) + ',' + str(program_name) + ',' + str(iteration) + ',' + str(ecomp) + ',' + str(CPU) + '\n')
data.close()
f.close()
