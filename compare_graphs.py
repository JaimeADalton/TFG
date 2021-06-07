#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st
import seaborn as sns
import os
import csv

with os.scandir('.') as directorios:
    directorios = [directorio.name for directorio in directorios if directorio.is_dir()]

if 'RawData' in directorios:
    directorios.pop(directorios.index('RawData'))
if 'compare_graphs' in directorios:
    directorios.pop(directorios.index('compare_graphs'))
if 'Plots' in directorios:
    directorios.pop(directorios.index('Plots'))

num_estudios = len(directorios)
for num_estudio in range(1,num_estudios + 1):
    break
    print(num_estudio)

    '''
    Tamaño de los archivos a comprimir segun # estudio.

    '''
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


    os.system('mkdir -p compare_graphs/')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/speed/')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/cpu/')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/rc')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/rc/7z')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/rc/clzip')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/rc/gzip')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/rc/lzop')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/rc/pbzip2')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/rc/pigz')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/rc/zip')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/dicc')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/dicc/7z')
    os.system('mkdir -p compare_graphs/Estudio_' + str(num_estudio) + '/dicc/clzip')


    '''
    Comparacion de ratios de compresion
    variable tamaños de diccionario
    constante nivel de compresion
    constante algoritmo
    constante programa
    '''

    def num_fix(list):
        digits = -2
        mx = max(list)
        mn = min(list)
        diff = f"{mx - mn:7f}"
        for digit in str(diff):
            if digit == '0':
                digits += 1
        return digits

    def ratio_compresion_diccionario_level3():
        data = open('ratio_results.txt', 'r')
        ratio = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 5 and iteracion > 0 and estudio == num_estudio:
                ratio.append(float(line[0]))
        data.close()
        maximo = max(ratio)
        fd4 = 0.7256


        plt.rcdefaults()
        fig, ax = plt.subplots()


        height = [ (element - fd4) / (maximo - fd4) for element in ratio ]
        bars = ('8 MiB', '16  MiB', '32  MiB', '64  MiB')
        x_pos = np.arange(len(bars))
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZMA - Level 3')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/dicc/7z/Ratio_C_7z-LZMA-3.png',  dpi=200,   quality=120,bbox_inches='tight')

    def ratio_compresion_diccionario_level5():
        data = open('ratio_results.txt', 'r')
        ratio = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 9 and iteracion > 4 and estudio == num_estudio:
                ratio.append(float(line[0]))
        data.close()
        maximo = max(ratio)
        fd4 = 0.79

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ (element - fd4) / (maximo - fd4) for element in ratio ]

        bars = ('8 MiB', '16  MiB', '32  MiB', '64  MiB')
        x_pos = np.arange(len(bars))
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZMA - Level 5')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/dicc/7z/Ratio_C_7z-LZMA-5.png',  dpi=200,   quality=120,bbox_inches='tight')

    def ratio_compresion_diccionario_level9():
        data = open('ratio_results.txt', 'r')
        ratio = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 13 and iteracion > 8 and estudio == num_estudio:
                ratio.append(float(line[0]))
        data.close()
        maximo = max(ratio)
        fd4 = 0.79


        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ (element - fd4) / (maximo - fd4) for element in ratio ]

        bars = ('8 MiB', '16  MiB', '32  MiB', '64  MiB')
        x_pos = np.arange(len(bars))
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZMA - Level 9')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/dicc/7z/Ratio_C_7z-LZMA-9.png',  dpi=200,   quality=120,bbox_inches='tight')

    def ratio_compresion_diccionario2_level3():
        data = open('ratio_results.txt', 'r')
        ratio = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion > 12 and iteracion < 17 and estudio == num_estudio:
                ratio.append(float(line[0]))
        data.close()
        maximo = max(ratio)
        fd4 = 0.7255


        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ (element - fd4) / (maximo - fd4) for element in ratio ]
        bars = ('8 MiB', '16  MiB', '32  MiB', '64  MiB')
        x_pos = np.arange(len(bars))
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZMA2 - Level 3')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/dicc/7z/Ratio_C_7z-LZMA2-3.png',  dpi=200,  quality=120,bbox_inches='tight')

    def ratio_compresion_diccionario2_level5():
        data = open('ratio_results.txt', 'r')
        ratio = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion > 16 and iteracion < 21 and estudio == num_estudio:
                ratio.append(float(line[0]))
        data.close()
        maximo = max(ratio)
        fd4 = 0.79

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ (element - fd4) / (maximo - fd4) for element in ratio ]

        bars = ('8 MiB', '16  MiB', '32  MiB', '64  MiB')
        x_pos = np.arange(len(bars))
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZMA2 - Level 5')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/dicc/7z/Ratio_C_7z-LZMA2-5.png',  dpi=200,  quality=120,bbox_inches='tight')

    def ratio_compresion_diccionario2_level9():
        data = open('ratio_results.txt', 'r')
        ratio = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion > 20 and iteracion < 25 and estudio == num_estudio:
                ratio.append(float(line[0]))
        data.close()
        maximo = max(ratio)
        fd4 = 0.79

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ (element - fd4) / (maximo - fd4) for element in ratio ]
        bars = ('8 MiB', '16  MiB', '32  MiB', '64  MiB')
        x_pos = np.arange(len(bars))
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZMA2 - Level 9')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/dicc/7z/Ratio_C_7z-LZMA2-9.png',  dpi=200,  quality=120,bbox_inches='tight')


    '''
    #####################################################################
                        DICTIONARY COMPARATION PLOTS
    #####################################################################
    '''

    def ratio_compresion_diccionario_clzip_LZMA():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []

        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 39 and iteracion > 33 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 44 and iteracion > 38 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion < 49 and iteracion > 43 and estudio == num_estudio:
                ratio3.append(float(line[0]))
        data.close()

        maximo1 = max(ratio1)
        maximo2 = max(ratio2)
        maximo3 = max(ratio3)
        fd41 = 0.745
        fd42 = 0.79
        fd43 = 0.79

        '''
        la diferencia es minima, para poder demostrarlo en la grafica eliminamos
        los primeros decimales que tienen los numeros en comun, ademas buscamos el
        maximo para divirilo por cada elemento y asi tener valores entre 0 y 1
        para una comparacion mas sencilla
        '''

        ratio1 = [ (element - fd41) / (maximo1 - fd41) for element in ratio1 ]
        ratio2 = [ (element - fd42) / (maximo2 - fd42) for element in ratio2 ]
        ratio3 = [ (element - fd43) / (maximo3 - fd43) for element in ratio3 ]

        index = ['2 Mib', '4 Mib', '8 Mib', '16 Mib', '32 Mib']

        df = pd.DataFrame({'Level 3': ratio1,'Level 6': ratio2, 'Level 9':ratio3},  index=index)
        axes = df.plot.bar(rot=0, subplots=True, title="Ratio de Compresion - LZMA - clzip", figsize=(8, 8), stacked=True)
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/dicc/clzip/Rati o_C_clzip.png',  dpi=200,    quality=120,   bbox_inches='tight')
        plt.close('all')

    def ratio_compresion_diccionario_7z_LZMA():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        ratio5 = []
        ratio6 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 5 and iteracion > 0 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 9 and iteracion > 4 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion < 13 and iteracion > 8 and estudio == num_estudio:
                ratio3.append(float(line[0]))
            if iteracion < 17 and iteracion > 12 and estudio == num_estudio:
                ratio4.append(float(line[0]))
            if iteracion < 21 and iteracion > 16 and estudio == num_estudio:
                ratio5.append(float(line[0]))
            if iteracion < 25 and iteracion > 20 and estudio == num_estudio:
                ratio6.append(float(line[0]))
        data.close()

        maximo1 = max(ratio1)
        maximo2 = max(ratio2)
        maximo3 = max(ratio3)
        maximo4 = max(ratio4)
        maximo5 = max(ratio5)
        maximo6 = max(ratio6)


        fd41 = 0.7256
        fd42 = 0.79
        fd43 = 0.79
        fd44 = 0.7255
        fd45 = 0.79
        fd46 = 0.79


        ratio1 = [ (element - fd41) / (maximo1 - fd41) for element in ratio1 ]
        ratio2 = [ (element - fd42) / (maximo2 - fd42) for element in ratio2 ]
        ratio3 = [ (element - fd43) / (maximo3 - fd43) for element in ratio3 ]
        ratio4 = [ (element - fd44) / (maximo4 - fd44) for element in ratio4 ]
        ratio5 = [ (element - fd45) / (maximo5 - fd45) for element in ratio5 ]
        ratio6 = [ (element - fd46) / (maximo6 - fd46) for element in ratio6 ]

        index = ['8 MiB', '16 MiB', '32 MiB', '64 MiB']

        df = pd.DataFrame({'LZMA - Level 3': ratio1,'LZMA - Level 6': ratio2, ' LZMA - Level 9':ratio3,'LZMA2 - Level 3': ratio4,'LZMA2 - Level 6':    ratio5, 'LZMA2 - Level 9':ratio6}, index=index)
        axes = df.plot.bar(rot=0, subplots=True, title="Rendimiento - 7z - LZMA/LZMA2",layout=(3,3), figsize=(10, 10), stacked= True)
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/dicc/7z/Ratio_C_7z.png' ,  dpi=200, quality=120, bbox_inches='tight')
        plt.close('all')


    '''
    #####################################################################
                 RATIO COMPRESSION BY DICTIONATY SIZE COMPARATION PLOTS
    #####################################################################

    Comparar nivel de compresion 3, 5 y 9, segun tamaño de diccionario

    '''

    def ratio_compresion_7z_level_LZMA_3_5_9():
        '''
        realizo una media de los valores de cada teracion corresponidente a un  tamaño de diccionario para tener valores concretos sobre los niveles de    compresion
        '''
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        for line in  csv.reader(data):
             estudio = int(line[1])
             iteracion = int(line[2  ])
             if iteracion < 5 and iteracion > 0 and estudio == num_estudio:
                 ratio1.append(float(line[0]))
             if iteracion < 9 and iteracion > 4 and estudio == num_estudio:
                 ratio2.append(float(line[0]))
             if iteracion < 13 and iteracion > 8 and estudio == num_estudio:
                 ratio3.append(float(line[0]))
        data.close()

        ratio1 = st.mean(ratio1)
        ratio2 = st.mean(ratio2)
        ratio3 = st.mean(ratio3)

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1, ratio2, ratio3 ]

        bars = ('Level 3', 'Level 5', 'Level 9')
        x_pos = np.arange(len(bars))

        fd41=0.7
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZMA')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/7z/rc_7z-LZMA.png',  dpi=200, quality=120)
        plt.close('all')



    def ratio_compresion_7z_level_LZMA2_3_5_9():
        '''
        realizo una media de los valores de cada teracion corresponidente a un  tamaño de diccionario para tener valores concretos sobre los niveles de    compresion
        '''
        data = open('ratio_results.txt', 'r')
        ratio4 = []
        ratio5 = []
        ratio6 = []
        for  line in  csv.reader(data):
             estudio = int(line[1])
             iteracion = int(line[2])
             if iteracion < 17 and iteracion > 12 and estudio == num_estudio:
                 ratio4.append(float(line[0]))
             if iteracion < 21 and iteracion > 16 and estudio == num_estudio:
                 ratio5.append(float(line[0]))
             if iteracion < 25 and iteracion > 20 and estudio == num_estudio:
                 ratio6.append(float(line[0]))
        data.close( )

        ratio4 = st.mean(ratio4)
        ratio5 = st.mean(ratio5)
        ratio6 = st.mean(ratio6)

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio4, ratio5, ratio6 ]
        bars = ('Level 3', 'Level 5', 'Level 9')
        x_pos = np.arange(len(bars))

        fd41=0.7
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZMA2')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/7z/rc_7z-LZMA2.png',  dpi=200, quality=120)
        plt.close('all')


    def ratio_compresion_clzip_level_LZMA_3_6_9():
        data = open('ratio_results.txt', 'r')
        ratio4 = []
        ratio5 = []
        ratio6 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 39 and iteracion > 33 and estudio == num_estudio:
                ratio4.append(float(line[0]))
            if iteracion < 44 and iteracion > 38 and estudio == num_estudio:
                ratio5.append(float(line[0]))
            if iteracion < 49 and iteracion > 43 and estudio == num_estudio:
                ratio6.append(float(line[0]))
        data.close()

        ratio4 = st.mean(ratio4)
        ratio5 = st.mean(ratio5)
        ratio6 = st.mean(ratio6)

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio4, ratio5, ratio6 ]
        bars = ('Level 3', 'Level 5', 'Level 9')
        x_pos = np.arange(len(bars))

        fd41=0.7
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZMA')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/clzip/rc_-LZMA.png',  dpi=200, quality=120)
        plt.close('all')


    '''
    #####################################################################
                 RATIO COMPRESSION COMPARATION PLOTS
    #####################################################################

    Comparar nivel de compresion 3-9

    '''


    def ratio_compresion_7z_level_deflate_3_5_9():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 25 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion == 26 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 27 and estudio == num_estudio:
                ratio3.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1[0], ratio2[0], ratio3[0] ]
        bars = ('Level 3', 'Level 5', 'Level 9')
        x_pos = np.arange(len(bars))

        fd41=0.7
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - Deflate')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/7z/rc_7z-Deflate.png',  dpi=200, quality=120 )
        plt.close('all')


    def ratio_compresion_7z_level_deflate64_3_5_9():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 28 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion == 29 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 30 and estudio == num_estudio:
                ratio3.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1[0], ratio2[0], ratio3[0] ]

        bars = ('Level 3', 'Level 5', 'Level 9')
        x_pos = np.arange(len(bars))

        fd41=0.7
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - Deflate64')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/7z/rc_7z-Deflate64.png',  dpi=200, quality=  120)
        plt.close('all')

    def ratio_compresion_7z_level_PPMD_3_5_9():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 31 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion == 32 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 33 and estudio == num_estudio:
                ratio3.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1[0], ratio2[0], ratio3[0] ]

        bars = ('Level 3', 'Level 5', 'Level 9')
        x_pos = np.arange(len(bars))

        fd41=0.8
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - PPMD')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/7z/rc_7z-PPMD.png',  dpi=200, quality=120)
        plt.close('all')

    def ratio_compresion_gzip():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 49 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion == 50 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 51 and estudio == num_estudio:
                ratio3.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1[0], ratio2[0], ratio3[0] ]

        bars = ('Level 3', 'Level 5', 'Level 9')
        x_pos = np.arange(len(bars))

        fd41=0.7
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]

        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - Deflate')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/gzip/rc_gzip-deflate.png',  dpi=200, quality =120)
        plt.close('all')


    def ratio_compresion_lzop():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 52 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion == 53 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 54 and estudio == num_estudio:
                ratio3.append(float(line[0]))
            if iteracion == 55 and estudio == num_estudio:
                ratio4.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1[0], ratio2[0], ratio3[0], ratio4[0]]
        bars = ('Level 3', 'Level 5', 'Level 7', 'Level 9')

        fd41=0.5
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]

        x_pos = np.arange(len(bars))
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - LZO')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/lzop/rc_LZO.png',  dpi=200, quality=120)
        plt.close('all')

    def ratio_compresion_pbzip2():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []

        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 56 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion == 57 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 58 and estudio == num_estudio:
                ratio3.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1[0], ratio2[0], ratio3[0]]


        bars = ('Level 3', 'Level 5', 'Level 9')
        x_pos = np.arange(len(bars))
        fd41=0.83
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - BWT')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/pbzip2/rc_bwt.png',  dpi=200, quality=120)
        plt.close('all')


    def ratio_compresion_pigz():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 59 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion == 60 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 61 and estudio == num_estudio:
                ratio3.append(float(line[0]))
            if iteracion == 62 and estudio == num_estudio:
                ratio4.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1[0], ratio2[0], ratio3[0], ratio4[0]]

        bars = ('Level 3', 'Level 5', 'Level 7', 'Level 9')

        x_pos = np.arange(len(bars))

        fd41=0.7
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]

        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - Deflate')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/pigz/rc_Deflate.png',  dpi=200, quality=120)
        plt.close('all')


    def ratio_compresion_zip_deflate():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 63 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion == 64 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 65 and estudio == num_estudio:
                ratio3.append(float(line[0]))
            if iteracion == 66 and estudio == num_estudio:
                ratio4.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1[0], ratio2[0], ratio3[0], ratio4[0]]

        bars = ('Level 3', 'Level 5', 'Level 7', 'Level 9')

        x_pos = np.arange(len(bars))

        fd41=0.7
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - Deflate')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/zip/rc_zip_deflate.png',  dpi=200, quality=  120)
        plt.close('all')


    def ratio_compresion_zip_bwt():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 67 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion == 68 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 69 and estudio == num_estudio:
                ratio3.append(float(line[0]))
            if iteracion == 70 and estudio == num_estudio:
                ratio4.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()
        height = [ ratio1[0], ratio2[0], ratio3[0], ratio4[0]]

        bars = ('Level 3', 'Level 5', 'Level 7', 'Level 9')

        x_pos = np.arange(len(bars))
        fd41=0.8
        maximo = max(height)
        height = [ (element - fd41) / (maximo - fd41) for element in height ]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Ratio de compresion - BWT')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/zip/rc_zip_bwt.png',  dpi=200, quality=120)
        plt.close('all')


    def ratio_compresion():
        data = open('ratio_results.txt', 'r')
        #ratio 3
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        ratio5 = []
        ratio6 = []
        ratio7 = []

        #ratio 5
        ratio12 = []
        ratio22 = []
        ratio32 = []
        ratio42 = []
        ratio52 = []
        ratio62 = []
        ratio72 = []

        #ratio 9
        ratio13 = []
        ratio23 = []
        ratio33 = []
        ratio43 = []
        ratio53 = []
        ratio63 = []
        ratio73 = []


        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 5 and iteracion > 0 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 17 and iteracion > 12 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 25 and estudio == num_estudio:
                ratio3.append(float(line[0]))
            if iteracion == 28 and estudio == num_estudio:
                ratio4.append(float(line[0]))
            if iteracion == 31 and estudio == num_estudio:
                ratio5.append(float(line[0]))
            if iteracion == 52 and estudio == num_estudio:
                ratio6.append(float(line[0]))
            if iteracion == 56 and estudio == num_estudio:
                ratio7.append(float(line[0]))

            if iteracion < 9 and iteracion > 4 and estudio == num_estudio:
                ratio12.append(float(line[0]))
            if iteracion < 21 and iteracion > 16 and estudio == num_estudio:
                ratio22.append(float(line[0]))
            if iteracion == 26 and estudio == num_estudio:
                ratio32.append(float(line[0]))
            if iteracion == 29 and estudio == num_estudio:
                ratio42.append(float(line[0]))
            if iteracion == 32 and estudio == num_estudio:
                ratio52.append(float(line[0]))
            if iteracion == 53 and estudio == num_estudio:
                ratio62.append(float(line[0]))
            if iteracion == 57 and estudio == num_estudio:
                ratio72.append(float(line[0]))


            if iteracion < 13 and iteracion > 8 and estudio == num_estudio:
                ratio13.append(float(line[0]))
            if iteracion < 25 and iteracion > 20 and estudio == num_estudio:
                ratio23.append(float(line[0]))
            if iteracion == 27 and estudio == num_estudio:
                ratio33.append(float(line[0]))
            if iteracion == 30 and estudio == num_estudio:
                ratio43.append(float(line[0]))
            if iteracion == 33 and estudio == num_estudio:
                ratio53.append(float(line[0]))
            if iteracion == 55 and estudio == num_estudio:
                ratio63.append(float(line[0]))
            if iteracion == 58 and estudio == num_estudio:
                ratio73.append(float(line[0]))

        ratio1 = st.mean(ratio1)
        ratio2 = st.mean(ratio2)

        ratio12 = st.mean(ratio12)
        ratio22 = st.mean(ratio22)

        ratio13 = st.mean(ratio13)
        ratio23 = st.mean(ratio23)

        data = [[ratio1,ratio2,ratio3[0],ratio4[0],ratio5[0],ratio6[0],ratio7[0]],[ratio12,ratio22,ratio32[0],ratio42[0],ratio52[0],ratio62[0],ratio72[0]], [ratio13,ratio23,ratio33[0],ratio43[0],ratio53[0],ratio63[0],ratio73[0]]]

        X = np.arange(7)
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])

        bars = ('LZMA', 'LZMA2', 'Deflate', 'Deflate64', 'PPMD', 'LZO', 'BWT')
        ax.bar(X + 0.00, data[0], color = 'tab:blue', width = 0.25)
        ax.bar(X + 0.25, data[1], color = 'tab:green', width = 0.25)
        ax.bar(X + 0.50, data[2], color = 'tab:orange', width = 0.25)
        ax.legend(labels=['Level 3', 'Level 5', 'Level 9'])

        plt.xticks(X + 0.25, bars)
        plt.title("Ratio de Compresion")
        plt.xlabel("Algoritmo")

        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/ratio-3-5-9.png',  dpi=200,  quality=120,bbox_inches='tight')
        plt.close('all')


    def deflate_compare():
        data = open('ratio_results.txt', 'r')
        level3 = []
        level5 = []
        level9 = []

        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion == 25 and estudio == num_estudio:
                level3.append(float(line[0]))
            if iteracion == 26 and estudio == num_estudio:
                level5.append(float(line[0]))
            if iteracion == 27 and estudio == num_estudio:
                level9.append(float(line[0]))
            if iteracion == 49 and estudio == num_estudio:
                level3.append(float(line[0]))
            if iteracion == 50 and estudio == num_estudio:
                level5.append(float(line[0]))
            if iteracion == 51 and estudio == num_estudio:
                level9.append(float(line[0]))
            if iteracion == 59 and estudio == num_estudio:
                level3.append(float(line[0]))
            if iteracion == 60 and estudio == num_estudio:
                level5.append(float(line[0]))
            if iteracion == 62 and estudio == num_estudio:
                level9.append(float(line[0]))
            if iteracion == 63 and estudio == num_estudio:
                level3.append(float(line[0]))
            if iteracion == 64 and estudio == num_estudio:
                level5.append(float(line[0]))
            if iteracion == 66 and estudio == num_estudio:
                level9.append(float(line[0]))
        data.close()

        plt.rcdefaults()
        fig, ax = plt.subplots()

        data = [level3, level5, level9]

        X = np.arange(4)
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])

        bars = ('7z', 'gzip', 'pigz', 'zip')
        ax.bar(X + 0.00, data[0], color = 'tab:blue', width = 0.25)
        ax.bar(X + 0.25, data[1], color = 'tab:green', width = 0.25)
        ax.bar(X + 0.50, data[2], color = 'tab:orange', width = 0.25)
        ax.legend(labels=['Level 3', 'Level 5', 'Level 9'])

        plt.xticks(X + 0.25, bars)
        plt.title("Ratio de Compresion - Deflate")
        plt.xlabel("Programa")

        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/deflate-3-5-9_all_programs.png',  dpi=200,  quality=120,bbox_inches='tight')
        plt.close('all')

    def overlap_barpgraph():
        data = open('ratio_results.txt', 'r')
        lzma_7z = []
        lzma2_7z = []
        Deflate_7z = []
        Deflate64_7z = []
        PPDM_7z = []
        LZMA_clzip = []
        Deflate_Gzip = []
        LZO_lzop = []
        BWT_pbzip2 = []
        Deflate_pigz = []
        Deflate_zip = []
        BWT_zip = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 13 and iteracion > 0 and estudio == num_estudio:
                lzma_7z.append(float(line[0]))
            if iteracion < 25 and iteracion > 12 and estudio == num_estudio:
                lzma2_7z.append(float(line[0]))
            if iteracion < 28 and iteracion > 24 and estudio == num_estudio:
                Deflate_7z.append(float(line[0]))
            if iteracion < 31 and iteracion > 27 and estudio == num_estudio:
                Deflate64_7z.append(float(line[0]))
            if iteracion < 34 and iteracion > 30 and estudio == num_estudio:
                PPDM_7z.append(float(line[0]))
            if iteracion < 49 and iteracion > 33 and estudio == num_estudio:
                LZMA_clzip.append(float(line[0]))
            if iteracion < 52 and iteracion > 48 and estudio == num_estudio:
                Deflate_Gzip.append(float(line[0]))
            if iteracion < 56 and iteracion > 51 and estudio == num_estudio:
                LZO_lzop.append(float(line[0]))
            if iteracion < 59 and iteracion > 55 and estudio == num_estudio:
                BWT_pbzip2.append(float(line[0]))
            if iteracion < 63 and iteracion > 58 and estudio == num_estudio:
                Deflate_pigz.append(float(line[0]))
            if iteracion < 67 and iteracion > 62 and estudio == num_estudio:
                Deflate_zip.append(float(line[0]))
            if iteracion < 71 and iteracion > 66 and estudio == num_estudio:
                BWT_zip.append(float(line[0]))

        data.close()

        LZMA_7z = st.mean(lzma_7z)
        LZMA_clzip = st.mean(LZMA_clzip)
        LZMA2_7z = st.mean(lzma2_7z)
        Deflate_7z = st.mean(Deflate_7z)
        Deflate_pigz = st.mean(Deflate_pigz)
        Deflate_zip = st.mean(Deflate_zip)
        Deflate_Gzip = st.mean(Deflate_Gzip)
        Deflate64_7z = st.mean(Deflate64_7z)
        BWT_pbzip2 = st.mean(BWT_pbzip2)
        BWT_zip = st.mean(BWT_zip)
        LZO_lzop = st.mean(LZO_lzop)
        PPDM_7z = st.mean(PPDM_7z)

        indices = np.arange(7)

        width = 0.8
        plt.xticks(indices, ['7z', 'clzip', 'gzip', 'lzop', 'pbzip2', 'pigz', 'zip'])

        lzma = [LZMA_7z, LZMA_clzip, 0, 0, 0, 0, 0]
        lzma2 = [LZMA2_7z, 0, 0, 0, 0, 0, 0]
        Deflate = [Deflate64_7z, 0, Deflate_Gzip, 0, 0, Deflate_pigz, Deflate_zip]
        Deflate_64 = [Deflate64_7z, 0, 0, 0, 0, 0, 0]
        BWT = [0,0,0,0, BWT_pbzip2 ,0, BWT_zip]
        LZO = [0, 0, 0, LZO_lzop, 0, 0, 0 ]
        PPDM = [PPDM_7z ,0 ,0, 0, 0, 0, 0]

        plt.bar(indices, lzma, width=width, color='tab:blue', label='LZMA')
        plt.bar(indices, lzma2, width=0.8*width, color='tab:orange', label='LZMA2')
        plt.bar(indices, Deflate, width=0.6*width, color='tab:green', label='Deflate')
        plt.bar(indices, Deflate_64, width=0.4*width, color='tab:red', label='Deflate64')
        plt.bar(indices, BWT, width=0.4*width, color='tab:purple', label='BWT')
        plt.bar(indices, LZO, width=0.8*width, color='tab:brown', label='LZO')
        plt.bar(indices, PPDM, width=0.2*width, color='tab:cyan', label='PPDM')


        plt.legend()
        # plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/rc/ratios_algoritmos_programa.png',  dpi=200,  quality=120,bbox_inches='tight')

        plt.close('all')


    '''
    #####################################################################
                 VELOCIDAD COMPARACION PLOTS SEGUN DICCIONARIO
    #####################################################################

    Comparar nivel de menor ratio y de mayor ratio de compresion segun algoritmo
    '''

    def velocidad_7z_lzma():
        data = open('time_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []

        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 5 and iteracion > 0 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 9 and iteracion > 4 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion < 13 and iteracion > 8 and estudio == num_estudio:
                ratio3.append(float(line[0]))
        data.close()

        ratio1 = [real_size/float(time) for time in ratio1]
        ratio2 = [real_size/float(time) for time in ratio2]
        ratio3 = [real_size/float(time) for time in ratio3]

        index = ['8 Mib', '16 Mib', '32 Mib', '64 Mib']

        df = pd.DataFrame({'Level 3': ratio1,'Level 6': ratio2, 'Level 9':ratio3},  index=index)
        axes = df.plot.bar(rot=0, subplots=True, title="Velocidad de Compresion - LZMA - 7z", figsize=(8, 8), stacked=True)
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/speed/Speed_7z_lzma_e' + str(num_estudio) + '.png',  dpi=200,    quality=120,   bbox_inches='tight')
        plt.close('all')

    def velocidad_7z_lzma2():
        data = open('time_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []

        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 17 and iteracion > 12 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 21 and iteracion > 16 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion < 25 and iteracion > 20 and estudio == num_estudio:
                ratio3.append(float(line[0]))
        data.close()

        ratio1 = [real_size/float(time) for time in ratio1]
        ratio2 = [real_size/float(time) for time in ratio2]
        ratio3 = [real_size/float(time) for time in ratio3]

        index = ['8 Mib', '16 Mib', '32 Mib', '64 Mib']

        df = pd.DataFrame({'Level 3': ratio1,'Level 6': ratio2, 'Level 9':ratio3},  index=index)
        axes = df.plot.bar(rot=0, subplots=True, title="Velocidad de Compresion - LZMA2 - 7z", figsize=(8, 8), stacked=True)
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/speed/Speed_7z_lzma2_e' + str(num_estudio) + '.png',  dpi=200,    quality=120,   bbox_inches='tight')
        plt.close('all')

    def velocidad_clzip_LZMA():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []

        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 39 and iteracion > 33 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 44 and iteracion > 38 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion < 49 and iteracion > 43 and estudio == num_estudio:
                ratio3.append(float(line[0]))
        data.close()

        index = ['2 Mib', '4 Mib', '8 Mib', '16 Mib', '32 Mib']

        ratio1 = [real_size/float(time) for time in ratio1]
        ratio2 = [real_size/float(time) for time in ratio2]
        ratio3 = [real_size/float(time) for time in ratio3]

        df = pd.DataFrame({'Level 3': ratio1,'Level 6': ratio2, 'Level 9':ratio3},  index=index)
        axes = df.plot.bar(rot=0, subplots=True, title="Velocidad de Compresion - LZMA  - clzip", figsize=(8, 8), stacked=True)
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/speed/Speed_clzip_LZMA_e' + str(num_estudio) + '.png',  dpi=200,    quality=120,   bbox_inches='tight')
        plt.close('all')

    def vel_level_3():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        ratio5 = []
        ratio6 = []
        ratio7 = []


        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 5 and iteracion > 0 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 17 and iteracion > 12 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 25 and estudio == num_estudio:
                ratio3.append(real_size/float(line[0]))
            if iteracion == 28 and estudio == num_estudio:
                ratio4.append(real_size/float(line[0]))
            if iteracion == 31 and estudio == num_estudio:
                ratio5.append(real_size/float(line[0]))
            if iteracion == 52 and estudio == num_estudio:
                ratio6.append(real_size/float(line[0]))
            if iteracion == 56 and estudio == num_estudio:
                ratio7.append(real_size/float(line[0]))

        ratio1 = st.mean([real_size/float(time) for time in ratio1])
        ratio2 = st.mean([real_size/float(time) for time in ratio2])


        plt.rcdefaults()
        fig, ax = plt.subplots()
        bars = ('LZMA', 'LZMA2', 'Deflate', 'Deflate64', 'PPMD', 'LZO', 'BWT')
        x_pos = np.arange(len(bars))

        height = [ratio1,ratio2,ratio3,ratio4,ratio5,ratio6,ratio7]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Velocidad - Level 3')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/speed/Speed-level-3.png',  dpi=200,  quality=120,bbox_inches='tight')

    def vel_level_5():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        ratio5 = []
        ratio6 = []
        ratio7 = []


        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 9 and iteracion > 4 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 21 and iteracion > 16 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 26 and estudio == num_estudio:
                ratio3.append(real_size/float(line[0]))
            if iteracion == 29 and estudio == num_estudio:
                ratio4.append(real_size/float(line[0]))
            if iteracion == 32 and estudio == num_estudio:
                ratio5.append(real_size/float(line[0]))
            if iteracion == 53 and estudio == num_estudio:
                ratio6.append(real_size/float(line[0]))
            if iteracion == 57 and estudio == num_estudio:
                ratio7.append(real_size/float(line[0]))

        ratio1 = st.mean([real_size/float(time) for time in ratio1])
        ratio2 = st.mean([real_size/float(time) for time in ratio2])

        plt.rcdefaults()
        fig, ax = plt.subplots()
        bars = ('LZMA', 'LZMA2', 'Deflate', 'Deflate64', 'PPMD', 'LZO', 'BWT')
        x_pos = np.arange(len(bars))

        height = [ratio1,ratio2,ratio3,ratio4,ratio5,ratio6,ratio7]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Velocidad - Level 5')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/speed/Speed-level-5.png',  dpi=200,  quality=120,bbox_inches='tight')

    def vel_level_9():
        data = open('ratio_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        ratio5 = []
        ratio6 = []
        ratio7 = []

        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 13 and iteracion > 8 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 25 and iteracion > 20 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 27 and estudio == num_estudio:
                ratio3.append(real_size/float(line[0]))
            if iteracion == 30 and estudio == num_estudio:
                ratio4.append(real_size/float(line[0]))
            if iteracion == 33 and estudio == num_estudio:
                ratio5.append(real_size/float(line[0]))
            if iteracion == 55 and estudio == num_estudio:
                ratio6.append(real_size/float(line[0]))
            if iteracion == 58 and estudio == num_estudio:
                ratio7.append(real_size/float(line[0]))

        ratio1 = st.mean([real_size/float(time) for time in ratio1])
        ratio2 = st.mean([real_size/float(time) for time in ratio2])

        plt.rcdefaults()
        fig, ax = plt.subplots()
        bars = ('LZMA', 'LZMA2', 'Deflate', 'Deflate64', 'PPMD', 'LZO', 'BWT')
        x_pos = np.arange(len(bars))
        height = [ratio1,ratio2,ratio3,ratio4,ratio5,ratio6,ratio7]
        plt.bar(x_pos, height)
        plt.xticks(x_pos, bars)
        plt.title('Velocidad - Level 9')
        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/speed/Speed-level-9.png',  dpi=200,  quality=120,bbox_inches='tight')

    def vel_level_3_5_9():
        data = open('time_results.txt', 'r')
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        ratio5 = []
        ratio6 = []
        ratio7 = []

        ratio12 = []
        ratio22 = []
        ratio32 = []
        ratio42 = []
        ratio52 = []
        ratio62 = []
        ratio72 = []

        ratio13 = []
        ratio23 = []
        ratio33 = []
        ratio43 = []
        ratio53 = []
        ratio63 = []
        ratio73 = []


        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 5 and iteracion > 0 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 17 and iteracion > 12 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 25 and estudio == num_estudio:
                ratio3.append(real_size/float(line[0]))
            if iteracion == 28 and estudio == num_estudio:
                ratio4.append(real_size/float(line[0]))
            if iteracion == 31 and estudio == num_estudio:
                ratio5.append(real_size/float(line[0]))
            if iteracion == 52 and estudio == num_estudio:
                ratio6.append(real_size/float(line[0]))
            if iteracion == 56 and estudio == num_estudio:
                ratio7.append(real_size/float(line[0]))

            if iteracion < 9 and iteracion > 4 and estudio == num_estudio:
                ratio12.append(float(line[0]))
            if iteracion < 21 and iteracion > 16 and estudio == num_estudio:
                ratio22.append(float(line[0]))
            if iteracion == 26 and estudio == num_estudio:
                ratio32.append(real_size/float(line[0]))
            if iteracion == 29 and estudio == num_estudio:
                ratio42.append(real_size/float(line[0]))
            if iteracion == 32 and estudio == num_estudio:
                ratio52.append(real_size/float(line[0]))
            if iteracion == 53 and estudio == num_estudio:
                ratio62.append(real_size/float(line[0]))
            if iteracion == 57 and estudio == num_estudio:
                ratio72.append(real_size/float(line[0]))


            if iteracion < 13 and iteracion > 8 and estudio == num_estudio:
                ratio13.append(float(line[0]))
            if iteracion < 25 and iteracion > 20 and estudio == num_estudio:
                ratio23.append(float(line[0]))
            if iteracion == 27 and estudio == num_estudio:
                ratio33.append(real_size/float(line[0]))
            if iteracion == 30 and estudio == num_estudio:
                ratio43.append(real_size/float(line[0]))
            if iteracion == 33 and estudio == num_estudio:
                ratio53.append(real_size/float(line[0]))
            if iteracion == 55 and estudio == num_estudio:
                ratio63.append(real_size/float(line[0]))
            if iteracion == 58 and estudio == num_estudio:
                ratio73.append(real_size/float(line[0]))

        ratio1 = st.mean([real_size/float(time) for time in ratio1])
        ratio2 = st.mean([real_size/float(time) for time in ratio2])

        ratio12 = st.mean([real_size/float(time) for time in ratio12])
        ratio22 = st.mean([real_size/float(time) for time in ratio22])

        ratio13 = st.mean([real_size/float(time) for time in ratio13])
        ratio23 = st.mean([real_size/float(time) for time in ratio23])

        data = [[ratio1,ratio2,ratio3,ratio4,ratio5,ratio6,ratio7],[ratio12,ratio22,ratio32,ratio42,ratio52,ratio62,ratio72], [ratio13,ratio23,ratio33,ratio43,ratio53,ratio63,ratio73]]

        X = np.arange(7)
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])

        bars = ('LZMA', 'LZMA2', 'Deflate', 'Deflate64', 'PPMD', 'LZO', 'BWT')
        ax.bar(X + 0.00, data[0], color = 'tab:blue', width = 0.25)
        ax.bar(X + 0.25, data[1], color = 'tab:green', width = 0.25)
        ax.bar(X + 0.50, data[2], color = 'tab:orange', width = 0.25)
        ax.legend(labels=['Level 3', 'Level 5', 'Level 9'])

        plt.xticks(X + 0.25, bars)
        plt.title("Velocidad de Compresion")
        plt.xlabel("Algoritmo")


        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/speed/Speed-level-3-5-9.png',  dpi=200,  quality=120,bbox_inches='tight')
        plt.close('all')


    '''
    ##################################################################
    #                            USO DE CPU % segun nivel
    ##################################################################

    '''

    def cpu_3_5_9():
        data = open('cpu_results.txt', 'r')
        #ratio 3
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        ratio5 = []
        ratio6 = []
        ratio7 = []

        #ratio 5
        ratio12 = []
        ratio22 = []
        ratio32 = []
        ratio42 = []
        ratio52 = []
        ratio62 = []
        ratio72 = []

        #ratio 9
        ratio13 = []
        ratio23 = []
        ratio33 = []
        ratio43 = []
        ratio53 = []
        ratio63 = []
        ratio73 = []


        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 5 and iteracion > 0 and estudio == num_estudio:
                ratio1.append(float(line[0]))
            if iteracion < 17 and iteracion > 12 and estudio == num_estudio:
                ratio2.append(float(line[0]))
            if iteracion == 25 and estudio == num_estudio:
                ratio3.append(float(line[0]))
            if iteracion == 28 and estudio == num_estudio:
                ratio4.append(float(line[0]))
            if iteracion == 31 and estudio == num_estudio:
                ratio5.append(float(line[0]))
            if iteracion == 52 and estudio == num_estudio:
                ratio6.append(float(line[0]))
            if iteracion == 56 and estudio == num_estudio:
                ratio7.append(float(line[0]))

            if iteracion < 9 and iteracion > 4 and estudio == num_estudio:
                ratio12.append(float(line[0]))
            if iteracion < 21 and iteracion > 16 and estudio == num_estudio:
                ratio22.append(float(line[0]))
            if iteracion == 26 and estudio == num_estudio:
                ratio32.append(float(line[0]))
            if iteracion == 29 and estudio == num_estudio:
                ratio42.append(float(line[0]))
            if iteracion == 32 and estudio == num_estudio:
                ratio52.append(float(line[0]))
            if iteracion == 53 and estudio == num_estudio:
                ratio62.append(float(line[0]))
            if iteracion == 57 and estudio == num_estudio:
                ratio72.append(float(line[0]))


            if iteracion < 13 and iteracion > 8 and estudio == num_estudio:
                ratio13.append(float(line[0]))
            if iteracion < 25 and iteracion > 20 and estudio == num_estudio:
                ratio23.append(float(line[0]))
            if iteracion == 27 and estudio == num_estudio:
                ratio33.append(float(line[0]))
            if iteracion == 30 and estudio == num_estudio:
                ratio43.append(float(line[0]))
            if iteracion == 33 and estudio == num_estudio:
                ratio53.append(float(line[0]))
            if iteracion == 55 and estudio == num_estudio:
                ratio63.append(float(line[0]))
            if iteracion == 58 and estudio == num_estudio:
                ratio73.append(float(line[0]))

        ratio1 = st.mean(ratio1)
        ratio2 = st.mean(ratio2)

        ratio12 = st.mean(ratio12)
        ratio22 = st.mean(ratio22)

        ratio13 = st.mean(ratio13)
        ratio23 = st.mean(ratio23)

        data = [[ratio1,ratio2,ratio3,ratio4,ratio5,ratio6,ratio7],[ratio12,ratio22,ratio32,ratio42,ratio52,ratio62,ratio72], [ratio13,ratio23,ratio33,ratio43,ratio53,ratio63,ratio73]]
        X = np.arange(7)
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])

        bars = ('LZMA', 'LZMA2', 'Deflate', 'Deflate64', 'PPMD', 'LZO', 'BWT')
        ax.bar(X + 0.00, data[0], color = 'tab:blue', width = 0.25)
        ax.bar(X + 0.25, data[1], color = 'tab:green', width = 0.25)
        ax.bar(X + 0.50, data[2], color = 'tab:orange', width = 0.25)
        ax.legend(labels=['Level 3', 'Level 5', 'Level 9'])

        plt.xticks(X + 0.25, bars)
        plt.title("CPU %")
        plt.xlabel("Algoritmo")

        plt.savefig('compare_graphs/Estudio_' + str(num_estudio) + '/cpu/Speed-level-3-5-9.png',  dpi=200,  quality=120,bbox_inches='tight')
        plt.close('all')

    if __name__ == '__main__':
        try:
            ratio_compresion_diccionario_clzip_LZMA()
            ratio_compresion_diccionario_7z_LZMA()
            ratio_compresion_7z_level_LZMA_3_5_9()
            ratio_compresion_7z_level_LZMA2_3_5_9()
            ratio_compresion_clzip_level_LZMA_3_6_9()
            ratio_compresion_7z_level_deflate_3_5_9()
            ratio_compresion_7z_level_deflate64_3_5_9()
            ratio_compresion_7z_level_PPMD_3_5_9()
            ratio_compresion_gzip()
            ratio_compresion_lzop()
            ratio_compresion_pbzip2()
            ratio_compresion_pigz()
            ratio_compresion_zip_deflate()
            ratio_compresion_zip_bwt()
            velocidad_7z_lzma()
            velocidad_7z_lzma2()
            velocidad_clzip_LZMA()
            vel_level_3()
            vel_level_5()
            vel_level_9()
            vel_level_3_5_9()
            cpu_3_5_9()
            ratio_compresion()
            deflate_compare()
            overlap_barpgraph()
        except:
            print(Error, "Estar seguro que todos los archivos y directorios existen tras ejecutar las pruebas: los errores que aparecen aqui es por que falta un directorio o un archivo .time o . du")

def overlap_barpgraph_txt():
        data = open('ratio_results.txt', 'r')
        lzma_7z = []
        lzma2_7z = []
        Deflate_7z = []
        Deflate64_7z = []
        PPDM_7z = []
        LZMA_clzip = []
        Deflate_Gzip = []
        LZO_lzop = []
        BWT_pbzip2 = []
        Deflate_pigz = []
        Deflate_zip = []
        BWT_zip = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 13 and iteracion > 0 and ( estudio == 1 or estudio == 2 or estudio == 3):
                lzma_7z.append(float(line[0]))
            if iteracion < 25 and iteracion > 12 and ( estudio == 1 or estudio == 2 or estudio == 3):
                lzma2_7z.append(float(line[0]))
            if iteracion < 28 and iteracion > 24 and ( estudio == 1 or estudio == 2 or estudio == 3):
                Deflate_7z.append(float(line[0]))
            if iteracion < 31 and iteracion > 27 and ( estudio == 1 or estudio == 2 or estudio == 3):
                Deflate64_7z.append(float(line[0]))
            if iteracion < 34 and iteracion > 30 and ( estudio == 1 or estudio == 2 or estudio == 3):
                PPDM_7z.append(float(line[0]))
            if iteracion < 49 and iteracion > 33 and ( estudio == 1 or estudio == 2 or estudio == 3):
                LZMA_clzip.append(float(line[0]))
            if iteracion < 52 and iteracion > 48 and ( estudio == 1 or estudio == 2 or estudio == 3):
                Deflate_Gzip.append(float(line[0]))
            if iteracion < 56 and iteracion > 51 and ( estudio == 1 or estudio == 2 or estudio == 3):
                LZO_lzop.append(float(line[0]))
            if iteracion < 59 and iteracion > 55 and ( estudio == 1 or estudio == 2 or estudio == 3):
                BWT_pbzip2.append(float(line[0]))
            if iteracion < 63 and iteracion > 58 and ( estudio == 1 or estudio == 2 or estudio == 3):
                Deflate_pigz.append(float(line[0]))
            if iteracion < 67 and iteracion > 62 and ( estudio == 1 or estudio == 2 or estudio == 3):
                Deflate_zip.append(float(line[0]))
            if iteracion < 71 and iteracion > 66 and ( estudio == 1 or estudio == 2 or estudio == 3):
                BWT_zip.append(float(line[0]))

        data.close()

        LZMA_7z = st.mean(lzma_7z)
        LZMA_clzip = st.mean(LZMA_clzip)
        LZMA2_7z = st.mean(lzma2_7z)
        Deflate_7z = st.mean(Deflate_7z)
        Deflate_pigz = st.mean(Deflate_pigz)
        Deflate_zip = st.mean(Deflate_zip)
        Deflate_Gzip = st.mean(Deflate_Gzip)
        Deflate64_7z = st.mean(Deflate64_7z)
        BWT_pbzip2 = st.mean(BWT_pbzip2)
        BWT_zip = st.mean(BWT_zip)
        LZO_lzop = st.mean(LZO_lzop)
        PPDM_7z = st.mean(PPDM_7z)

        indices = np.arange(7)

        width = 0.8
        plt.xticks(indices, ['7z', 'clzip', 'gzip', 'lzop', 'pbzip2', 'pigz', 'zip'])

        lzma = [LZMA_7z, LZMA_clzip, 0, 0, 0, 0, 0]
        lzma2 = [LZMA2_7z, 0, 0, 0, 0, 0, 0]
        Deflate = [Deflate64_7z, 0, Deflate_Gzip, 0, 0, Deflate_pigz, Deflate_zip]
        Deflate_64 = [Deflate64_7z, 0, 0, 0, 0, 0, 0]
        BWT = [0,0,0,0, BWT_pbzip2 ,0, BWT_zip]
        LZO = [0, 0, 0, LZO_lzop, 0, 0, 0 ]
        PPDM = [PPDM_7z ,0 ,0, 0, 0, 0, 0]

        plt.bar(indices, lzma, width=width, color='tab:blue', label='LZMA')
        plt.bar(indices, lzma2, width=0.8*width, color='tab:orange', label='LZMA2')
        plt.bar(indices, Deflate, width=0.6*width, color='tab:green', label='Deflate')
        plt.bar(indices, Deflate_64, width=0.4*width, color='tab:red', label='Deflate64')
        plt.bar(indices, BWT, width=0.4*width, color='tab:purple', label='BWT')
        plt.bar(indices, LZO, width=0.8*width, color='tab:brown', label='LZO')
        plt.bar(indices, PPDM, width=0.2*width, color='tab:cyan', label='PPDM')

        plt.title("Ratios de compresión - TXT", loc="center")
        plt.legend()
        plt.savefig('compare_graphs/ratios_algoritmos_programa_txt.png',  dpi=200,  quality=120,bbox_inches='tight')

        plt.close('all')

def overlap_barpgraph_doc():
        data = open('ratio_results.txt', 'r')
        lzma_7z = []
        lzma2_7z = []
        Deflate_7z = []
        Deflate64_7z = []
        PPDM_7z = []
        LZMA_clzip = []
        Deflate_Gzip = []
        LZO_lzop = []
        BWT_pbzip2 = []
        Deflate_pigz = []
        Deflate_zip = []
        BWT_zip = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 13 and iteracion > 0 and ( estudio == 6 or estudio == 7 or estudio == 8):
                lzma_7z.append(float(line[0]))
            if iteracion < 25 and iteracion > 12 and ( estudio == 6 or estudio == 7 or estudio == 8):
                lzma2_7z.append(float(line[0]))
            if iteracion < 28 and iteracion > 24 and ( estudio == 6 or estudio == 7 or estudio == 8):
                Deflate_7z.append(float(line[0]))
            if iteracion < 31 and iteracion > 27 and ( estudio == 6 or estudio == 7 or estudio == 8):
                Deflate64_7z.append(float(line[0]))
            if iteracion < 34 and iteracion > 30 and ( estudio == 6 or estudio == 7 or estudio == 8):
                PPDM_7z.append(float(line[0]))
            if iteracion < 49 and iteracion > 33 and ( estudio == 6 or estudio == 7 or estudio == 8):
                LZMA_clzip.append(float(line[0]))
            if iteracion < 52 and iteracion > 48 and ( estudio == 6 or estudio == 7 or estudio == 8):
                Deflate_Gzip.append(float(line[0]))
            if iteracion < 56 and iteracion > 51 and ( estudio == 6 or estudio == 7 or estudio == 8):
                LZO_lzop.append(float(line[0]))
            if iteracion < 59 and iteracion > 55 and ( estudio == 6 or estudio == 7 or estudio == 8):
                BWT_pbzip2.append(float(line[0]))
            if iteracion < 63 and iteracion > 58 and ( estudio == 6 or estudio == 7 or estudio == 8):
                Deflate_pigz.append(float(line[0]))
            if iteracion < 67 and iteracion > 62 and ( estudio == 6 or estudio == 7 or estudio == 8):
                Deflate_zip.append(float(line[0]))
            if iteracion < 71 and iteracion > 66 and ( estudio == 6 or estudio == 7 or estudio == 8):
                BWT_zip.append(float(line[0]))

        data.close()

        LZMA_7z = st.mean(lzma_7z)
        LZMA_clzip = st.mean(LZMA_clzip)
        LZMA2_7z = st.mean(lzma2_7z)
        Deflate_7z = st.mean(Deflate_7z)
        Deflate_pigz = st.mean(Deflate_pigz)
        Deflate_zip = st.mean(Deflate_zip)
        Deflate_Gzip = st.mean(Deflate_Gzip)
        Deflate64_7z = st.mean(Deflate64_7z)
        BWT_pbzip2 = st.mean(BWT_pbzip2)
        BWT_zip = st.mean(BWT_zip)
        LZO_lzop = st.mean(LZO_lzop)
        PPDM_7z = st.mean(PPDM_7z)

        indices = np.arange(7)

        width = 0.8
        plt.xticks(indices, ['7z', 'clzip', 'gzip', 'lzop', 'pbzip2', 'pigz', 'zip'])

        lzma = [LZMA_7z, LZMA_clzip, 0, 0, 0, 0, 0]
        lzma2 = [LZMA2_7z, 0, 0, 0, 0, 0, 0]
        Deflate = [Deflate64_7z, 0, Deflate_Gzip, 0, 0, Deflate_pigz, Deflate_zip]
        Deflate_64 = [Deflate64_7z, 0, 0, 0, 0, 0, 0]
        BWT = [0,0,0,0, BWT_pbzip2 ,0, BWT_zip]
        LZO = [0, 0, 0, LZO_lzop, 0, 0, 0 ]
        PPDM = [PPDM_7z ,0 ,0, 0, 0, 0, 0]

        plt.bar(indices, lzma, width=width, color='tab:blue', label='LZMA')
        plt.bar(indices, lzma2, width=0.8*width, color='tab:orange', label='LZMA2')
        plt.bar(indices, PPDM, width=0.6*width, color='tab:cyan', label='PPDM')
        plt.bar(indices, BWT, width=0.8*width, color='tab:purple', label='BWT')
        plt.bar(indices, Deflate, width=0.4*width, color='tab:green', label='Deflate')
        plt.bar(indices, Deflate_64, width=0.2*width, color='tab:red', label='Deflate64')
        plt.bar(indices, LZO, width=0.8*width, color='tab:brown', label='LZO')

        plt.title("Ratios de compresión - DOC", loc="center")
        plt.legend()
        plt.savefig('compare_graphs/ratios_algoritmos_programa_doc.png',  dpi=200,  quality=120,bbox_inches='tight')
        plt.close('all')

def overlap_barpgraph_pdf():
        data = open('ratio_results.txt', 'r')
        lzma_7z = []
        lzma2_7z = []
        Deflate_7z = []
        Deflate64_7z = []
        PPDM_7z = []
        LZMA_clzip = []
        Deflate_Gzip = []
        LZO_lzop = []
        BWT_pbzip2 = []
        Deflate_pigz = []
        Deflate_zip = []
        BWT_zip = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 13 and iteracion > 0 and estudio == 4:
                lzma_7z.append(float(line[0]))
            if iteracion < 25 and iteracion > 12 and estudio == 4:
                lzma2_7z.append(float(line[0]))
            if iteracion < 28 and iteracion > 24 and estudio == 4:
                Deflate_7z.append(float(line[0]))
            if iteracion < 31 and iteracion > 27 and estudio == 4:
                Deflate64_7z.append(float(line[0]))
            if iteracion < 34 and iteracion > 30 and estudio == 4:
                PPDM_7z.append(float(line[0]))
            if iteracion < 49 and iteracion > 33 and estudio == 4:
                LZMA_clzip.append(float(line[0]))
            if iteracion < 52 and iteracion > 48 and estudio == 4:
                Deflate_Gzip.append(float(line[0]))
            if iteracion < 56 and iteracion > 51 and estudio == 4:
                LZO_lzop.append(float(line[0]))
            if iteracion < 59 and iteracion > 55 and estudio == 4:
                BWT_pbzip2.append(float(line[0]))
            if iteracion < 63 and iteracion > 58 and estudio == 4:
                Deflate_pigz.append(float(line[0]))
            if iteracion < 67 and iteracion > 62 and estudio == 4:
                Deflate_zip.append(float(line[0]))
            if iteracion < 71 and iteracion > 66 and estudio == 4:
                BWT_zip.append(float(line[0]))

        data.close()

        LZMA_7z = st.mean(lzma_7z)
        LZMA_clzip = st.mean(LZMA_clzip)
        LZMA2_7z = st.mean(lzma2_7z)
        Deflate_7z = st.mean(Deflate_7z)
        Deflate_pigz = st.mean(Deflate_pigz)
        Deflate_zip = st.mean(Deflate_zip)
        Deflate_Gzip = st.mean(Deflate_Gzip)
        Deflate64_7z = st.mean(Deflate64_7z)
        BWT_pbzip2 = st.mean(BWT_pbzip2)
        BWT_zip = st.mean(BWT_zip)
        LZO_lzop = st.mean(LZO_lzop)
        PPDM_7z = st.mean(PPDM_7z)

        indices = np.arange(7)

        width = 0.8
        plt.xticks(indices, ['7z', 'clzip', 'gzip', 'lzop', 'pbzip2', 'pigz', 'zip'])

        lzma = [LZMA_7z, LZMA_clzip, 0, 0, 0, 0, 0]
        lzma2 = [LZMA2_7z, 0, 0, 0, 0, 0, 0]
        Deflate = [Deflate64_7z, 0, Deflate_Gzip, 0, 0, Deflate_pigz, Deflate_zip]
        Deflate_64 = [Deflate64_7z, 0, 0, 0, 0, 0, 0]
        BWT = [0,0,0,0, BWT_pbzip2 ,0, BWT_zip]
        LZO = [0, 0, 0, LZO_lzop, 0, 0, 0 ]
        PPDM = [PPDM_7z ,0 ,0, 0, 0, 0, 0]

        plt.bar(indices, lzma, width=width, color='tab:blue', label='LZMA')
        plt.bar(indices, lzma2, width=0.8*width, color='tab:orange', label='LZMA2')
        plt.bar(indices, PPDM, width=0.6*width, color='tab:cyan', label='PPDM')
        plt.bar(indices, BWT, width=0.8*width, color='tab:purple', label='BWT')
        plt.bar(indices, Deflate, width=0.4*width, color='tab:green', label='Deflate')
        plt.bar(indices, Deflate_64, width=0.2*width, color='tab:red', label='Deflate64')
        plt.bar(indices, LZO, width=0.8*width, color='tab:brown', label='LZO')

        plt.title("Ratios de compresión - PDF", loc="center")
        plt.legend()
        plt.savefig('compare_graphs/ratios_algoritmos_programa_pdf.png',  dpi=200,  quality=120,bbox_inches='tight')
        plt.close('all')

def overlap_barpgraph_xml():
        data = open('ratio_results.txt', 'r')
        lzma_7z = []
        lzma2_7z = []
        Deflate_7z = []
        Deflate64_7z = []
        PPDM_7z = []
        LZMA_clzip = []
        Deflate_Gzip = []
        LZO_lzop = []
        BWT_pbzip2 = []
        Deflate_pigz = []
        Deflate_zip = []
        BWT_zip = []
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 13 and iteracion > 0 and estudio == 5:
                lzma_7z.append(float(line[0]))
            if iteracion < 25 and iteracion > 12 and estudio == 5:
                lzma2_7z.append(float(line[0]))
            if iteracion < 28 and iteracion > 24 and estudio == 5:
                Deflate_7z.append(float(line[0]))
            if iteracion < 31 and iteracion > 27 and estudio == 5:
                Deflate64_7z.append(float(line[0]))
            if iteracion < 34 and iteracion > 30 and estudio == 5:
                PPDM_7z.append(float(line[0]))
            if iteracion < 49 and iteracion > 33 and estudio == 5:
                LZMA_clzip.append(float(line[0]))
            if iteracion < 52 and iteracion > 48 and estudio == 5:
                Deflate_Gzip.append(float(line[0]))
            if iteracion < 56 and iteracion > 51 and estudio == 5:
                LZO_lzop.append(float(line[0]))
            if iteracion < 59 and iteracion > 55 and estudio == 5:
                BWT_pbzip2.append(float(line[0]))
            if iteracion < 63 and iteracion > 58 and estudio == 5:
                Deflate_pigz.append(float(line[0]))
            if iteracion < 67 and iteracion > 62 and estudio == 5:
                Deflate_zip.append(float(line[0]))
            if iteracion < 71 and iteracion > 66 and estudio == 5:
                BWT_zip.append(float(line[0]))

        data.close()

        LZMA_7z = st.mean(lzma_7z)
        LZMA_clzip = st.mean(LZMA_clzip)
        LZMA2_7z = st.mean(lzma2_7z)
        Deflate_7z = st.mean(Deflate_7z)
        Deflate_pigz = st.mean(Deflate_pigz)
        Deflate_zip = st.mean(Deflate_zip)
        Deflate_Gzip = st.mean(Deflate_Gzip)
        Deflate64_7z = st.mean(Deflate64_7z)
        BWT_pbzip2 = st.mean(BWT_pbzip2)
        BWT_zip = st.mean(BWT_zip)
        LZO_lzop = st.mean(LZO_lzop)
        PPDM_7z = st.mean(PPDM_7z)

        indices = np.arange(7)

        width = 0.8
        plt.xticks(indices, ['7z', 'clzip', 'gzip', 'lzop', 'pbzip2', 'pigz', 'zip'])

        lzma = [LZMA_7z, LZMA_clzip, 0, 0, 0, 0, 0]
        lzma2 = [LZMA2_7z, 0, 0, 0, 0, 0, 0]
        Deflate = [Deflate64_7z, 0, Deflate_Gzip, 0, 0, Deflate_pigz, Deflate_zip]
        Deflate_64 = [Deflate64_7z, 0, 0, 0, 0, 0, 0]
        BWT = [0,0,0,0, BWT_pbzip2 ,0, BWT_zip]
        LZO = [0, 0, 0, LZO_lzop, 0, 0, 0 ]
        PPDM = [PPDM_7z ,0 ,0, 0, 0, 0, 0]

        plt.bar(indices, lzma, width=width, color='tab:blue', label='LZMA')
        plt.bar(indices, lzma2, width=0.8*width, color='tab:orange', label='LZMA2')
        plt.bar(indices, PPDM, width=0.6*width, color='tab:cyan', label='PPDM')
        plt.bar(indices, BWT, width=0.8*width, color='tab:purple', label='BWT')
        plt.bar(indices, Deflate, width=0.4*width, color='tab:green', label='Deflate')
        plt.bar(indices, Deflate_64, width=0.2*width, color='tab:red', label='Deflate64')
        plt.bar(indices, LZO, width=0.8*width, color='tab:brown', label='LZO')

        plt.title("Ratios de compresión - XML", loc="center")
        plt.legend()
        plt.savefig('compare_graphs/ratios_algoritmos_programa_xml.png',  dpi=200,  quality=120,bbox_inches='tight')
        plt.close('all')


def distribucion_ratio_all():
    data = open('ratio_results.txt', 'r')
    lzma_7z = []
    lzma2_7z = []
    Deflate_7z = []
    Deflate64_7z = []
    PPDM_7z = []
    LZMA_clzip = []
    Deflate_Gzip = []
    LZO_lzop = []
    BWT_pbzip2 = []
    Deflate_pigz = []
    Deflate_zip = []
    BWT_zip = []
    for line in csv.reader(data):
        estudio = int(line[1])
        iteracion = int(line[2])
        if iteracion < 13 and iteracion > 0:
            lzma_7z.append(float(line[0]))
        if iteracion < 25 and iteracion > 12:
            lzma2_7z.append(float(line[0]))
        if iteracion < 28 and iteracion > 24:
            Deflate_7z.append(float(line[0]))
        if iteracion < 31 and iteracion > 27:
            Deflate64_7z.append(float(line[0]))
        if iteracion < 34 and iteracion > 30:
            PPDM_7z.append(float(line[0]))
        if iteracion < 49 and iteracion > 33:
            LZMA_clzip.append(float(line[0]))
        if iteracion < 52 and iteracion > 48:
            Deflate_Gzip.append(float(line[0]))
        if iteracion < 56 and iteracion > 51:
            LZO_lzop.append(float(line[0]))
        if iteracion < 59 and iteracion > 55:
            BWT_pbzip2.append(float(line[0]))
        if iteracion < 63 and iteracion > 58:
            Deflate_pigz.append(float(line[0]))
        if iteracion < 67 and iteracion > 62:
            Deflate_zip.append(float(line[0]))
        if iteracion < 71 and iteracion > 66:
            BWT_zip.append(float(line[0]))
    data.close()

    LZMA = lzma_7z + LZMA_clzip
    Deflate = Deflate_7z + Deflate_Gzip + Deflate_pigz + Deflate_zip
    BWT = BWT_pbzip2 + BWT_zip

    a = pd.DataFrame({ 'Algoritmo' : np.repeat('LZMA',len(LZMA)), 'value': LZMA })
    b = pd.DataFrame({ 'Algoritmo' : np.repeat('LZMA2',len(lzma2_7z)), 'value': lzma2_7z })
    c = pd.DataFrame({ 'Algoritmo' : np.repeat('Deflate',len(Deflate)), 'value': Deflate })
    d = pd.DataFrame({ 'Algoritmo' : np.repeat('Deflate64',len(Deflate64_7z)), 'value': Deflate64_7z })
    e = pd.DataFrame({ 'Algoritmo' : np.repeat('BWT',len(BWT)), 'value': BWT })
    f = pd.DataFrame({ 'Algoritmo' : np.repeat('LZO',len(LZO_lzop)), 'value': LZO_lzop })
    g = pd.DataFrame({ 'Algoritmo' : np.repeat('PPMD',len(PPDM_7z)), 'value': PPDM_7z })
    df=a.append(b).append(c).append(d).append(e).append(f).append(g)

    ax = sns.boxplot(x='Algoritmo', y='value', data=df)
    # ax = sns.stripplot(x='Algoritmo', y='value', data=df, color="orange", jitter=0.2, size=2.5)
    plt.title("Distribución de los ratios de compresión", loc="center")
    plt.savefig('compare_graphs/ratios_algoritmos_distribucion.png',  dpi=200,  quality=120,bbox_inches='tight')
    plt.close('all')


def ecomp_all():
    data = open('ecomp_results.txt', 'r')
    lzma_7z = []
    lzma2_7z = []
    Deflate_7z = []
    Deflate64_7z = []
    PPDM_7z = []
    LZMA_clzip = []
    Deflate_Gzip = []
    LZO_lzop = []
    BWT_pbzip2 = []
    Deflate_pigz = []
    Deflate_zip = []
    BWT_zip = []
    for line in csv.reader(data):
        estudio = int(line[0])
        iteracion = int(line[2])
        if iteracion < 13 and iteracion > 0:
            lzma_7z.append(float(line[3]))
        if iteracion < 25 and iteracion > 12:
            lzma2_7z.append(float(line[3]))
        if iteracion < 28 and iteracion > 24:
            Deflate_7z.append(float(line[3]))
        if iteracion < 31 and iteracion > 27:
            Deflate64_7z.append(float(line[3]))
        if iteracion < 34 and iteracion > 30:
            PPDM_7z.append(float(line[3]))
        if iteracion < 49 and iteracion > 33:
            LZMA_clzip.append(float(line[3]))
        if iteracion < 52 and iteracion > 48:
            Deflate_Gzip.append(float(line[3]))
        if iteracion < 56 and iteracion > 51:
            LZO_lzop.append(float(line[3]))
        if iteracion < 59 and iteracion > 55:
            BWT_pbzip2.append(float(line[3]))
        if iteracion < 63 and iteracion > 58:
            Deflate_pigz.append(float(line[3]))
        if iteracion < 67 and iteracion > 62:
            Deflate_zip.append(float(line[3]))
        if iteracion < 71 and iteracion > 66:
            BWT_zip.append(float(line[3]))
    data.close()
    LZMA_7z = st.mean(lzma_7z)
    LZMA_clzip = st.mean(LZMA_clzip)
    LZMA2_7z = st.mean(lzma2_7z)
    Deflate_7z = st.mean(Deflate_7z)
    Deflate_pigz = st.mean(Deflate_pigz)
    Deflate_zip = st.mean(Deflate_zip)
    Deflate_Gzip = st.mean(Deflate_Gzip)
    Deflate64_7z = st.mean(Deflate64_7z)
    BWT_pbzip2 = st.mean(BWT_pbzip2)
    BWT_zip = st.mean(BWT_zip)
    LZO_lzop = st.mean(LZO_lzop)
    PPDM_7z = st.mean(PPDM_7z)
    indices = np.arange(7)
    width = 0.8
    plt.xticks(indices, ['7z', 'clzip', 'gzip', 'lzop', 'pbzip2', 'pigz', 'zip'])
    lzma = [LZMA_7z, LZMA_clzip, 0, 0, 0, 0, 0]
    lzma2 = [LZMA2_7z, 0, 0, 0, 0, 0, 0]
    Deflate = [Deflate64_7z, 0, Deflate_Gzip, 0, 0, Deflate_pigz, Deflate_zip]
    Deflate_64 = [Deflate64_7z, 0, 0, 0, 0, 0, 0]
    BWT = [0,0,0,0, BWT_pbzip2 ,0, BWT_zip]
    LZO = [0, 0, 0, LZO_lzop, 0, 0, 0 ]
    PPDM = [PPDM_7z ,0 ,0, 0, 0, 0, 0]
    plt.bar(indices, lzma, width=width, color='tab:blue', label='LZMA')
    plt.bar(indices, lzma2, width=0.8*width, color='tab:orange', label='LZMA2')
    plt.bar(indices, PPDM, width=0.6*width, color='tab:cyan', label='PPDM')
    plt.bar(indices, BWT, width=0.8*width, color='tab:purple', label='BWT')
    plt.bar(indices, Deflate, width=0.4*width, color='tab:green', label='Deflate')
    plt.bar(indices, Deflate_64, width=0.2*width, color='tab:red', label='Deflate64')
    plt.bar(indices, LZO, width=0.8*width, color='tab:brown', label='LZO')
    plt.title("Eficiencia de Compresion", loc="center")
    plt.legend()
    plt.savefig('compare_graphs/recomp_all.png',  dpi=200,  quality=120,bbox_inches='tight')
    plt.close('all')

def ratio_compresion_all():
        data = open('ratio_results.txt', 'r')
        #ratio 3
        ratio1 = []
        ratio2 = []
        ratio3 = []
        ratio4 = []
        ratio5 = []
        ratio6 = []
        ratio7 = []

        #ratio 5
        ratio12 = []
        ratio22 = []
        ratio32 = []
        ratio42 = []
        ratio52 = []
        ratio62 = []
        ratio72 = []

        #ratio 9
        ratio13 = []
        ratio23 = []
        ratio33 = []
        ratio43 = []
        ratio53 = []
        ratio63 = []
        ratio73 = []


        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])

            if iteracion < 5 and iteracion > 0:
                ratio1.append(float(line[0]))
            if iteracion < 17 and iteracion > 12:
                ratio2.append(float(line[0]))
            if iteracion == 25:
                ratio3.append(float(line[0]))
            if iteracion == 28:
                ratio4.append(float(line[0]))
            if iteracion == 31:
                ratio5.append(float(line[0]))
            if iteracion == 52:
                ratio6.append(float(line[0]))
            if iteracion == 56:
                ratio7.append(float(line[0]))

            if iteracion < 9 and iteracion > 4:
                ratio12.append(float(line[0]))
            if iteracion < 21 and iteracion > 16:
                ratio22.append(float(line[0]))
            if iteracion == 26:
                ratio32.append(float(line[0]))
            if iteracion == 29:
                ratio42.append(float(line[0]))
            if iteracion == 32:
                ratio52.append(float(line[0]))
            if iteracion == 53:
                ratio62.append(float(line[0]))
            if iteracion == 57:
                ratio72.append(float(line[0]))


            if iteracion < 13 and iteracion > 8:
                ratio13.append(float(line[0]))
            if iteracion < 25 and iteracion > 20:
                ratio23.append(float(line[0]))
            if iteracion == 27:
                ratio33.append(float(line[0]))
            if iteracion == 30:
                ratio43.append(float(line[0]))
            if iteracion == 33:
                ratio53.append(float(line[0]))
            if iteracion == 55:
                ratio63.append(float(line[0]))
            if iteracion == 58:
                ratio73.append(float(line[0]))

        ratio1 = st.median(ratio1)
        ratio2 = st.median(ratio2)
        ratio3 = st.median(ratio3)
        ratio4 = st.median(ratio4)
        ratio5 = st.median(ratio5)
        ratio6 = st.median(ratio6)
        ratio7 = st.median(ratio7)
        ratio12 = st.median(ratio12)
        ratio22 = st.median(ratio22)
        ratio32 = st.median(ratio32)
        ratio42 = st.median(ratio42)
        ratio52 = st.median(ratio52)
        ratio62 = st.median(ratio62)
        ratio72 = st.median(ratio72)
        ratio13 = st.median(ratio13)
        ratio23 = st.median(ratio23)
        ratio33 = st.median(ratio33)
        ratio43 = st.median(ratio43)
        ratio53 = st.median(ratio53)
        ratio63 = st.median(ratio63)
        ratio73 = st.median(ratio73)

        data = [[ratio1,ratio2,ratio3,ratio4,ratio5,ratio6,ratio7],[ratio12,ratio22,ratio32,ratio42,ratio52,ratio62,ratio72], [ratio13,ratio23,ratio33,ratio43,ratio53,ratio63,ratio73]]

        X = np.arange(7)
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])

        bars = ('LZMA', 'LZMA2', 'Deflate', 'Deflate64', 'PPMD', 'LZO', 'BWT')
        ax.bar(X + 0.00, data[0], color = 'tab:blue', width = 0.25)
        ax.bar(X + 0.25, data[1], color = 'tab:green', width = 0.25)
        ax.bar(X + 0.50, data[2], color = 'tab:orange', width = 0.25)
        ax.legend(labels=['Level 3', 'Level 5', 'Level 9'])

        plt.xticks(X + 0.25, bars)
        plt.title("Ratio de Compresion")
        plt.xlabel("Algoritmo")

        plt.savefig('compare_graphs/ratio-3-5-9_all.png',  dpi=200,  quality=120,bbox_inches='tight')
        plt.close('all')

def vel_level_3_5_9_all():
    data = open('time_results.txt', 'r')
    ratio1 = []
    ratio2 = []
    ratio3 = []
    ratio4 = []
    ratio5 = []
    ratio6 = []
    ratio7 = []
    ratio12 = []
    ratio22 = []
    ratio32 = []
    ratio42 = []
    ratio52 = []
    ratio62 = []
    ratio72 = []
    ratio13 = []
    ratio23 = []
    ratio33 = []
    ratio43 = []
    ratio53 = []
    ratio63 = []
    ratio73 = []
    for estudio in range(1,9):
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
        for line in csv.reader(data):
            estudio = int(line[1])
            iteracion = int(line[2])
            if iteracion < 5 and iteracion > 0 and estudio == num_estudio:
                ratio1.append(real_size/float(line[0]))
            if iteracion < 17 and iteracion > 12 and estudio == num_estudio:
                ratio2.append(real_size/float(line[0]))
            if iteracion == 25 and estudio == num_estudio:
                ratio3.append(real_size/float(line[0]))
            if iteracion == 28 and estudio == num_estudio:
                ratio4.append(real_size/float(line[0]))
            if iteracion == 31 and estudio == num_estudio:
                ratio5.append(real_size/float(line[0]))
            if iteracion == 52 and estudio == num_estudio:
                ratio6.append(real_size/float(line[0]))
            if iteracion == 56 and estudio == num_estudio:
                ratio7.append(real_size/float(line[0]))
            if iteracion < 9 and iteracion > 4 and estudio == num_estudio:
                ratio12.append(float(real_size/float(line[0])))
            if iteracion < 21 and iteracion > 16 and estudio == num_estudio:
                ratio22.append(float(real_size/float(line[0])))
            if iteracion == 26 and estudio == num_estudio:
                ratio32.append(real_size/float(line[0]))
            if iteracion == 29 and estudio == num_estudio:
                ratio42.append(real_size/float(line[0]))
            if iteracion == 32 and estudio == num_estudio:
                ratio52.append(real_size/float(line[0]))
            if iteracion == 53 and estudio == num_estudio:
                ratio62.append(real_size/float(line[0]))
            if iteracion == 57 and estudio == num_estudio:
                ratio72.append(real_size/float(line[0]))
            if iteracion < 13 and iteracion > 8 and estudio == num_estudio:
                ratio13.append(float(real_size/float(line[0])))
            if iteracion < 25 and iteracion > 20 and estudio == num_estudio:
                ratio23.append(float(real_size/float(line[0])))
            if iteracion == 27 and estudio == num_estudio:
                ratio33.append(real_size/float(line[0]))
            if iteracion == 30 and estudio == num_estudio:
                ratio43.append(real_size/float(line[0]))
            if iteracion == 33 and estudio == num_estudio:
                ratio53.append(real_size/float(line[0]))
            if iteracion == 55 and estudio == num_estudio:
                ratio63.append(real_size/float(line[0]))
            if iteracion == 58 and estudio == num_estudio:
                ratio73.append(real_size/float(line[0]))
    ratio1 = st.mean(ratio1)
    ratio2 = st.mean(ratio2)
    ratio3 = st.mean(ratio3)
    ratio4 = st.mean(ratio4)
    ratio5 = st.mean(ratio5)
    ratio6 = st.mean(ratio6)
    ratio7 = st.mean(ratio7)
    ratio12 = st.mean(ratio12)
    ratio22 = st.mean(ratio22)
    ratio32 = st.mean(ratio32)
    ratio42 = st.mean(ratio42)
    ratio52 = st.mean(ratio52)
    ratio62 = st.mean(ratio62)
    ratio72 = st.mean(ratio72)
    ratio13 = st.mean(ratio13)
    ratio23 = st.mean(ratio23)
    ratio33 = st.mean(ratio33)
    ratio43 = st.mean(ratio43)
    ratio53 = st.mean(ratio53)
    ratio63 = st.mean(ratio63)
    ratio73 = st.mean(ratio73)

    data = [[ratio1,ratio2,ratio3,ratio4,ratio5,ratio6,ratio7],[ratio12,ratio22,ratio32,ratio42,ratio52,ratio62,ratio72], [ratio13,ratio23,ratio33,ratio43,ratio53,ratio63,ratio73]]
    X = np.arange(7)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    bars = ('LZMA', 'LZMA2', 'Deflate', 'Deflate64', 'PPMD', 'LZO', 'BWT')
    ax.bar(X + 0.00, data[0], color = 'tab:blue', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'tab:green', width = 0.25)
    ax.bar(X + 0.50, data[2], color = 'tab:orange', width = 0.25)
    ax.legend(labels=['Level 3', 'Level 5', 'Level 9'])
    plt.xticks(X + 0.25, bars)
    plt.title("Velocidad de Compresion")
    plt.xlabel("Algoritmo")
    plt.savefig('compare_graphs/Speed-level-3-5-9_all.png',  dpi=200,  quality=120,bbox_inches='tight')
    plt.close('all')

def cpu_3_5_9_all():
    data = open('cpu_results.txt', 'r')
    #ratio 3
    ratio1 = []
    ratio2 = []
    ratio3 = []
    ratio4 = []
    ratio5 = []
    ratio6 = []
    ratio7 = []
    #ratio 5
    ratio12 = []
    ratio22 = []
    ratio32 = []
    ratio42 = []
    ratio52 = []
    ratio62 = []
    ratio72 = []
    #ratio 9
    ratio13 = []
    ratio23 = []
    ratio33 = []
    ratio43 = []
    ratio53 = []
    ratio63 = []
    ratio73 = []
    for line in csv.reader(data):
        estudio = int(line[1])
        iteracion = int(line[2])
        if iteracion < 5 and iteracion > 0:
            ratio1.append(float(line[0]))
        if iteracion < 17 and iteracion > 12:
            ratio2.append(float(line[0]))
        if iteracion == 25:
            ratio3.append(float(line[0]))
        if iteracion == 28:
            ratio4.append(float(line[0]))
        if iteracion == 31:
            ratio5.append(float(line[0]))
        if iteracion == 52:
            ratio6.append(float(line[0]))
        if iteracion == 56:
            ratio7.append(float(line[0]))
        if iteracion < 9 and iteracion > 4:
            ratio12.append(float(line[0]))
        if iteracion < 21 and iteracion > 16:
            ratio22.append(float(line[0]))
        if iteracion == 26:
            ratio32.append(float(line[0]))
        if iteracion == 29:
            ratio42.append(float(line[0]))
        if iteracion == 32:
            ratio52.append(float(line[0]))
        if iteracion == 53:
            ratio62.append(float(line[0]))
        if iteracion == 57:
            ratio72.append(float(line[0]))
        if iteracion < 13 and iteracion > 8:
            ratio13.append(float(line[0]))
        if iteracion < 25 and iteracion > 20:
            ratio23.append(float(line[0]))
        if iteracion == 27:
            ratio33.append(float(line[0]))
        if iteracion == 30:
            ratio43.append(float(line[0]))
        if iteracion == 33:
            ratio53.append(float(line[0]))
        if iteracion == 55:
            ratio63.append(float(line[0]))
        if iteracion == 58:
            ratio73.append(float(line[0]))

    data = [[st.mean(ratio1),st.mean(ratio2),st.mean(ratio3),st.mean(ratio4),st.mean(ratio5),st.mean(ratio6),st.mean(ratio7)],
    [st.mean(ratio12),st.mean(ratio22),st.mean(ratio32),st.mean(ratio42),st.mean(ratio52),st.mean(ratio62),st.mean(ratio72)],
    [st.mean(ratio13),st.mean(ratio23),st.mean(ratio33),st.mean(ratio43),st.mean(ratio53),st.mean(ratio63),st.mean(ratio73)]]

    X = np.arange(7)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    bars = ('LZMA', 'LZMA2', 'Deflate', 'Deflate64', 'PPMD', 'LZO', 'BWT')
    ax.bar(X + 0.00, data[0], color = 'tab:blue', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'tab:green', width = 0.25)
    ax.bar(X + 0.50, data[2], color = 'tab:orange', width = 0.25)
    ax.legend(labels=['Level 3', 'Level 5', 'Level 9'])
    plt.xticks(X + 0.25, bars)
    plt.title("CPU %")
    plt.xlabel("Algoritmo")
    plt.savefig('compare_graphs/cpu-level-3-5-9.png',  dpi=200,  quality=120,bbox_inches='tight')
    plt.close('all')

def cpu_usage():
    data = open('cpu_results.txt', 'r')
    Sietez = []
    clzip = []
    gzip = []
    lzop = []
    pbzip2 = []
    pigz = []
    Zip = []
    for line in csv.reader(data):
        iteracion = int(line[2])
        if iteracion >= 0 and iteracion <= 33:
            Sietez.append(int(line[0]))
        if iteracion >= 34 and iteracion <= 48:
            clzip.append(int(line[0]))
        if iteracion >= 49 and iteracion <= 51:
            gzip.append(int(line[0]))
        if iteracion >= 52 and iteracion <= 55:
           lzop.append(int(line[0]))
        if iteracion >= 56 and iteracion <= 58:
           pbzip2.append(int(line[0]))
        if iteracion >= 59 and iteracion <= 62:
           pigz.append(int(line[0]))
        if iteracion >= 63 and iteracion <= 70:
           Zip.append(int(line[0]))

    data = [[max(Sietez), max(clzip), max(gzip), max(lzop), max(pbzip2), max(pigz), max(Zip)],
            [min(Sietez), min(clzip), min(gzip), min(lzop), min(pbzip2), min(pigz), min(Zip)]]

    X = np.arange(7)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    bars = ('7Z', 'clzip', 'gzip', 'lzop', 'pbzip2', 'pigz', 'zip')
    ax.bar(X + 0.00, data[0], color = 'tab:blue', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'tab:green', width = 0.25)

    ax.legend(labels=['Maximo', 'Minimo'])

    plt.xticks(X + 0.125, bars)
    plt.xlabel("Programa")
    plt.ylabel("%")
    plt.title("Uso maximo y minimo de CPU %", loc="center")
    plt.savefig('compare_graphs/uso_CPU_Programa.png',  dpi=200,  quality=120,bbox_inches='tight')
    plt.close('all')




# ##############################################################################
#                                      INIT
# ##############################################################################


# overlap_barpgraph_txt()
# overlap_barpgraph_doc()
# distribucion_ratio_all()
# overlap_barpgraph_pdf()
# overlap_barpgraph_xml()
# ecomp_all()
# ratio_compresion_all()
# vel_level_3_5_9_all()
# cpu_3_5_9_all()
# cpu_usage()




###############################################################################

#                                  circular plot

###############################################################################

# import matplotlib.pyplot as plt
# import pandas as pd
# from math import pi
# import csv

# real_size = 10485760


# estudio = []
# program = []
# iteracion = []
# size = []
# time = []
# cpu = []



# data = open('TimeDuData.txt', 'r')
# for line in csv.reader(data):
#             estudio.append(int(line[0]))
#             program.append(line[1])
#             iteracion.append(int(line[2]))
#             size.append(int(line[3]))
#             time.append(float(line[4]))
#             cpu.append(int(line[7])/10)



# size = [ element / real_size * 100 for element in size]

# time = [ element / time[size.index(element)] * 10 for element in size]

# for j in range(0,len(time),3):

#     # Set data
#     # df = pd.DataFrame({'group': ['A','B','C'],'CPU %': [0, 10, 20],'Comp.': [10, 20, 30],'Vel.': [20, 30, 0]})

#     df = pd.DataFrame({'group': ['A','B','C'],'CPU %': [cpu[j], cpu[j+1], cpu[j+2]],'Comp.': [size[j], size[j+1], size[j+2]],'Ecomp.': [time[j+0], time[j+1], time[j+2]]})

#     print(df)
#     #------- PART 1: Create background

#     # number of variable

#     categories=list(df)[1:]
#     N = len(categories)

#     # What will be the angle of each axis in the plot? (we divide the plot / number of variable)

#     angles = [n / float(N) * 2 * pi for n in range(N)]
#     angles += angles[:1]

#     # Initialise the spider plot
#     ax = plt.subplot(111, polar=True)

#     # If you want the first axis to be on top:
#     ax.set_theta_offset(pi / 2)
#     ax.set_theta_direction(-1)

#     # Draw one axe per variable + add labels
#     plt.xticks(angles[:-1], categories)

#     # Draw ylabels
#     ax.set_rlabel_position(0)
#     plt.yticks([20,40,60], ["20","40","60"], color="grey", size=7)
#     plt.ylim(0,80)


#     # ------- PART 2: Add plots

#     # Plot each individual = each line of the data
#     # I don't make a loop, because plotting more than 3 groups makes the chart unreadable

#     # Ind1
#     values=df.loc[0].drop('group').values.flatten().tolist()
#     values += values[:1]
#     ax.plot(angles, values, linewidth=1, linestyle='solid', label="Nivel 3")
#     ax.fill(angles, values, 'b', alpha=0.1)

#     # Ind2
#     values=df.loc[1].drop('group').values.flatten().tolist()
#     values += values[:1]
#     ax.plot(angles, values, linewidth=1, linestyle='solid', label="Nivel 5")
#     ax.fill(angles, values, 'r', alpha=0.1)

#     # Ind2
#     values=df.loc[2].drop('group').values.flatten().tolist()
#     values += values[:1]
#     ax.plot(angles, values, linewidth=1, linestyle='solid', label="Nivel 7")
#     ax.fill(angles, values, 'r', alpha=0.1)

#     # Add legend
#     plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

#     # Show the graph
#     plt.show()
