#!/usr/bin/python3

'''
Este Script recopilará los datos del estudio del Proyecto de Fin de Grado - ASIR 2019/2020
Describiré diferentes funciones que recopilaran los datos de las pruebas, serán almacenadas en formato CSV.
Los datos que recopilaré son:
    RAM usado por la aplicacion
    Uso de lectura de disco
    Uso de escritura de disco
    Uso de procesador
'''
import time
import psutil
import sys
import os
import subprocess

start_time = time.time()

try:
    software_name = str(sys.argv[1])
    number = str(sys.argv[2])
except IndexError:
    print("No ha introducido el nombre del programa")
    quit()

os.system('mkdir -p Datos/%s/%s/' % (software_name, number))
# os.system('mkdir -p TimeData/%s/%s/' % (software_name, number))
# os.system('mkdir -p DuData/%s/%s/' % (software_name, number))

def Process_Active():
        bashcmd = "ps aux | grep %s | grep -v 'grep %s' | grep -v python3 | awk '{print $2}'" % (software_name,software_name)
        PID = subprocess.check_output(bashcmd, shell=True)
        end_time = time.time()
        if len(str(PID)) > 3:
            return True
        elif (end_time - start_time) < 5:
            return True
        else:
            time.sleep(1)
            return False

def RawData():

    VMemdata = open("Datos/%s/%s/vmemory.txt"                                  % (software_name, number), 'w+')
    CPUTimesdata = open("Datos/%s/%s/cputimes.txt"                             % (software_name, number), 'w+')
    CPUStatsdata = open("Datos/%s/%s/cpustats.txt"                             % (software_name, number), 'w+')
    CPUFreqdata = open("Datos/%s/%s/cpufreq.txt"                               % (software_name, number),'w+')
    CPUPercentdata = open("Datos/%s/%s/CPUPercent.txt"                         % (software_name, number), 'w+')
    DiskIOdata = open("Datos/%s/%s/Diskiocounters.txt"                         % (software_name, number), 'w+')

    while Process_Active():
        time.sleep(0.1)

        VMem, CPUTimes, CPUStats, CPUFreq, CPUPercent, DiskIO = psutil.virtual_memory(), psutil.cpu_times(), psutil.cpu_stats(), psutil.cpu_freq(), psutil.cpu_percent(percpu=True), psutil.disk_io_counters()


        print(f"{CPUTimes[0]},{CPUTimes[ 1 ]},{CPUTimes[ 2 ]},                 {CPUTimes[ 3 ]},{CPUTimes[ 4 ]},{CPUTimes[ 5 ]},                   {CPUTimes[ 6 ]},{CPUTimes[ 7 ]},{CPUTimes[ 8 ]},                   {CPUTimes[ 9 ]}", file=CPUTimesdata)

        print(f"{CPUPercent[ 0 ]},{CPUPercent[ 1 ]},{CPUPercent[ 2 ]},         {CPUPercent[ 3 ]},{CPUPercent[ 4 ]},{CPUPercent[ 5 ]},             {CPUPercent[ 6 ]},{CPUPercent[ 7 ]}", file=CPUPercentdata)

        print(f"{DiskIO[ 0 ]},{DiskIO[ 1 ]},{DiskIO[ 2 ]},                     {DiskIO[ 3 ]},{DiskIO[ 4 ]},{DiskIO[ 5 ]},                         {DiskIO[ 6 ]},{DiskIO[ 7 ]},{DiskIO[ 8 ]}", file=DiskIOdata)

        print(f"{VMem[ 1 ]},{VMem[ 3 ]},{VMem[ 4 ]},                           {VMem[ 5 ]},{VMem[ 6 ]},{VMem[ 7 ]},                               {VMem[ 8 ]},{VMem[ 9 ]}", file=VMemdata)

        print(f"{CPUStats[ 0 ]},{CPUStats[ 1 ]},{CPUStats[ 2 ]}",            file=CPUStatsdata)

        print(f"{int(CPUFreq[ 0 ])}", file=CPUFreqdata)

    VMemdata.close()
    CPUTimesdata.close()
    CPUStatsdata.close()
    CPUFreqdata.close()
    CPUPercentdata.close()
    DiskIOdata.close()

if __name__ == '__main__':
    RawData()
