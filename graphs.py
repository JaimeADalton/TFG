#!/usr/bin/env python

# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import os
import sys
from matplotlib.ticker import StrMethodFormatter

Estudio_Dir=sys.argv[1]

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def cpufreq():
    os.system('mkdir -p Plots/' + str(Estudio_Dir) + '/cpufreq')
    paths = find_all('cpufreq.txt',Estudio_Dir)


    for path in paths:
        cpufreq = []
        numrow = 0
        with open(path,'r') as data:
            for line in csv.reader(data):
                cpufreq.append(int(line[0]))
                numrow += 1
        # use the plot function
        plt.plot(cpufreq)
        plt.xlim(0,numrow)
        plt.ylim(500,4100)
        program = path.split('/')[-3]
        iteration = path.split('/')[-2]

        plt.suptitle("Frecuencia CPU - "+program.upper(), fontsize=13, fontweight=0, color='black', style='italic')
        plt.xlabel("Tiempo (0.1 s)")
        plt.ylabel("Frecuencia MHz")
        # show the graph
        plt.savefig("Plots/" + str(Estudio_Dir) + "/cpufreq/" + program + "_" + iteration + "_" + 'cpufreq_graph.png', dpi=380, quality=120,bbox_inches='tight')
        plt.clf()

def cpupercent():
    os.system('mkdir -p Plots/' + str(Estudio_Dir) + '/cpupercent')

    paths = find_all('CPUPercent.txt',Estudio_Dir)
    for path in paths:
        cpu1 = []
        cpu2 = []
        cpu3 = []
        cpu4 = []
        cpu5 = []
        cpu6 = []
        cpu7 = []
        cpu8 = []

        numrow = 0
        with open(path,'r') as data:
           for line in csv.reader(data):
                    cpu1.append(float(line[0]))
                    cpu2.append(float(line[1]))
                    cpu3.append(float(line[2]))
                    cpu4.append(float(line[3]))
                    cpu5.append(float(line[4]))
                    cpu6.append(float(line[5]))
                    cpu7.append(float(line[6]))
                    cpu8.append(float(line[7]))
                    numrow += 1

        max_data = max(max([ x for x in cpu1 ]),
                       max([ x for x in cpu2 ]),
                       max([ x for x in cpu3 ]),
                       max([ x for x in cpu4 ]),
                       max([ x for x in cpu5 ]),
                       max([ x for x in cpu6 ]),
                       max([ x for x in cpu7 ]),
                       max([ x for x in cpu8 ]))


        # Make a data frame
        df=pd.DataFrame({'x': [float(x) for x in range(1,len(cpu1)+1)],
                        'CPU 1': cpu1,
                        'CPU 2': cpu2,
                        'CPU 3': cpu3,
                        'CPU 4': cpu4,
                        'CPU 5': cpu5,
                        'CPU 6': cpu6,
                        'CPU 7': cpu7,
                        'CPU 8': cpu8
                        })


        # Initialize the figure style
        #plt.style.use('seaborn-darkgrid')

        # create a color palette
        palette = plt.get_cmap('Set1')

        # multiple line plot
        num=0
        for column in df.drop('x', axis=1):
            num+=1

            # Find the right spot on the plot
            plt.subplot(4,2, num)

            # Plot the lineplot
            plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=0.9, alpha=0.9, label=column)


            # Same limits for every chart
            plt.xlim(0,numrow)
            plt.ylim(0,float(max_data))
            #plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

            plt.tight_layout(pad=1.0)

            #if num in range(7) :
            # plt.tick_params(labelbottom='off')
            # plt.tick_params(labelleft='on')

            # Add title
            plt.title(column, loc='right', fontsize=10, fontweight=1, color=palette(num) )


        program = path.split('/')[-3]
        # general title
        plt.suptitle("CPU Percent - "+program.upper(), fontsize=13, fontweight=0, color='black', style='italic')
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])

        # Axis titles
        plt.text(0, 0, 'T = 0.1s', ha='left', va='top')
        #plt.text(0.06, 0.5, 'Process', ha='center', va='center', rotation='vertical')


        iteration = path.split('/')[-2]
        # Show the graph
        plt.savefig("Plots/" + str(Estudio_Dir) + "/cpupercent/" + program + "_" + iteration + "_" + 'cpupercent_graph.png', dpi=200, quality=120,bbox_inches='tight',pad_inches=0.5)
        plt.clf()

def cpustats():
    os.system('mkdir -p Plots/' + str(Estudio_Dir) + '/cpustats')
    paths = find_all('cpustats.txt',Estudio_Dir)
    for path in paths:

        ctx_switches = []
        interrupts = []
        soft_interrupts = []


        with open(path,'r') as data:
           for line in csv.reader(data):
                    ctx_switches.append(int(line[0]))
                    interrupts.append(int(line[1]))
                    soft_interrupts.append(int(line[2]))

        ctx_switches_min = min(ctx_switches)
        interrupts_min = min(interrupts)
        soft_interrupts_min = min(soft_interrupts)



        ctx_switches_list = [ element - ctx_switches_min for element in ctx_switches]
        interrupts_list = [ element - interrupts_min for element in interrupts]
        soft_interrupts_list = [ element - soft_interrupts_min for element in soft_interrupts]


        # Make a data frame

        df=pd.DataFrame({'x': range(1,len(soft_interrupts)+1),
                        'ctx_switches':  ctx_switches_list,
                        'interrupts': interrupts_list,
                        'soft_interrupts': soft_interrupts_list
                        })

        ctx_switches_max = max(ctx_switches_list)
        interrupts_max = max(interrupts_list)
        soft_interrupts_max = max(soft_interrupts_list)

        max_data = max([ctx_switches_max,interrupts_max,soft_interrupts_max ])

        # Initialize the figure style
        plt.style.use('seaborn-darkgrid')

        # create a color palette
        palette = plt.get_cmap('Set1')

        # multiple line plot
        num=0
        for column in df.drop('x', axis=1):
            num+=1

            # Find the right spot on the plot
            plt.subplot(3,3, num)

            # Plot the lineplot
            plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1.9, alpha=0.9, label=column)

            # Same limits for every chart
            plt.xlim(0,len(soft_interrupts)+1)
            plt.ylim(0,max_data)
            plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

            # Not ticks everywhere
            if num in range(7) :
                plt.tick_params(labelbottom='off')
            if num not in [len(soft_interrupts)] :
                plt.tick_params(labelleft='off')

            # Add title
            plt.title(column, loc='right', fontsize=10, fontweight=1, color=palette(num) )

        program = path.split('/')[-3]
        # general title
        plt.suptitle("CPU Stats - "+program.upper(), fontsize=13, fontweight=0, color='black', style='italic')



        # Axis titles
        plt.text(0, 0, 'Tiempo', ha='left', va='top')
        #plt.text(0.06, 0.5, 'Process', ha='center', va='center', rotation='vertical')
        iteration = path.split('/')[-2]
        # Show the graph
        print("cpustats/" + program + "_" + iteration + "_" + 'cpustats_graph.png')
        plt.savefig("Plots/" + str(Estudio_Dir) + "/cpustats/" + program + "_" + iteration + "_" + 'cpustats_graph.png', dpi=200, quality=120,bbox_inches='tight')
        plt.clf()

def cputimes():
    os.system('mkdir -p Plots/' + str(Estudio_Dir) + '/cputimes')
    paths = find_all('cputimes.txt',Estudio_Dir)

    for path in paths:

        user = []
        nice = []
        system = []
        idle = []
        iowait = []
        irq = []
        softirq = []
        steal = []
        guest = []
        guest_nice = []

        numrow = -1
        with open(path,'r') as data:
            for line in csv.reader(data):
                try:
                    user.append(float(line[0]))
                    nice.append(float(line[1]))
                    system.append(float(line[2]))
                    idle.append(float(line[3]))
                    iowait.append(float(line[4]))
                    irq.append(float(line[5]))
                    softirq.append(float(line[6]))
                    steal.append(float(line[7]))
                    guest.append(float(line[8]))
                    guest_nice.append(float(line[9]))
                    numrow += 1
                except:
                    pass


        max_data = {'user': max([ x for x in user ]),
                    'nice': max([ x for x in nice ]),
                    'system': max([ x for x in system ]),
                    'idle': max([ x for x in idle ]),
                    'iowait': max([ x for x in iowait ]),
                    'irq': max([ x for x in irq ]),
                    'softirq': max([ x for x in softirq ]),
                    'steal': max([ x for x in steal ]),
                    'guest': max([ x for x in guest ]),
                    'guest_nice': max([ x for x in guest_nice ])}

        min_data = {'user': min([ x for x in user ]),
                    'nice': min([ x for x in nice ]),
                    'system': min([ x for x in system ]),
                    'idle': min([ x for x in idle ]),
                    'iowait': min([ x for x in iowait ]),
                    'irq': min([ x for x in irq ]),
                    'softirq': min([ x for x in softirq ]),
                    'steal': min([ x for x in steal ]),
                    'guest': min([ x for x in guest ]),
                    'guest_nice': min([ x for x in guest_nice ])}

        df=pd.DataFrame({'x': range(len(user)),
                        'user': [ x %8000 for x in user],
                        'nice': [ x %8000 for x in nice],
                        'system': [ x %8000 for x in system],
                        'idle':  [ x %8000 for x in idle],
                        'iowait': [ x %8000 for x in iowait],
                        'irq': [ x %8000 for x in irq],
                        'softirq': [ x %8000 for x in softirq]
                        })

        # Change the style of plot
        plt.style.use('seaborn-darkgrid')

        # set figure size
        my_dpi=96
        plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)

        program = path.split('/')[-3]
        # general title
        plt.suptitle("CPU Percent - "+program.upper(), fontsize=13, fontweight=0, color='black', style='italic')

        # plot multiple lines
        for column in df.drop('x', axis=1):
            plt.plot(df['x'], df[column], marker='', color='grey', linewidth=1, alpha=0.4)

        # Now re do the interesting curve, but biger with distinct color
        plt.plot(df['x'], df['system'], marker='', color='orange', linewidth=2, alpha=0.5)

        # Change x axis limit
        plt.xlim(0,len(user))

        # Let's annotate the plot
        num=0
        for i in df.values[9][1:]:
            num+=1
            name=list(df)[num]
            if name != 'system':
                plt.text(10.2, i, name, horizontalalignment='left', size='small', color='grey')

        # And add a special annotation for the group we are interested in
        plt.text(10.2, df.system.tail(1), 'System', horizontalalignment='left', size='small', color='orange')

        # Add titles
        plt.title("Actividad de los modos de la CPU", loc='left', fontsize=12, fontweight=0, color='black')
        plt.xlabel("Time")
        plt.ylabel("Score")
        iteration = path.split('/')[-2]

        # Show the graph
        plt.savefig("Plots/" + str(Estudio_Dir) + "/cputimes/" + program + "_" + iteration + "_" + 'cputimes_graph.png', dpi=200, quality=120,bbox_inches='tight',pad_inches=0.5)
        plt.clf()
        plt.close('all')

def diskiocounters():
    os.system('mkdir -p Plots/' + str(Estudio_Dir) + '/diskiocounters')
    paths = find_all('Diskiocounters.txt',Estudio_Dir)

    for path in paths:

        read_count = []
        write_count = []
        read_bytes = []
        write_bytes = []
        read_time = []
        write_time = []
        busy_time = []
        read_merged_count = []
        write_merged_count = []
        write_merged_count_write_count = []

        numrow = 0
        with open(path,'r') as data:
            for line in csv.reader(data):
                try:
                    read_count.append(float(line[0]))
                    write_count.append(float(line[1]))
                    read_bytes.append(float(line[2]))
                    write_bytes.append(float(line[3]))
                    read_time.append(float(line[4]))
                    write_time.append(float(line[5]))
                    busy_time.append(float(line[6]))
                    read_merged_count.append(float(line[7]))
                    write_merged_count.append(float(line[8]))
                    numrow += 1
                except:
                    pass


        max_data = {'read_count': max(read_count),
                    'write_count': max(write_count),
                    'read_bytes': max(read_bytes),
                    'write_bytes': max(write_bytes),
                    'read_time': max(read_time),
                    'write_time': max(write_time),
                    'busy_time': max(busy_time),
                    'read_merged': max(read_merged_count),
                    'write_merged': max(write_merged_count)}

        min_data = {'read_count': min(read_count),
                    'write_count': min(write_count),
                    'read_bytes': min(read_bytes),
                    'write_bytes': min(write_bytes),
                    'read_time': min(read_time),
                    'write_time': min(write_time),
                    'busy_time': min(busy_time),
                    'read_merged': min(read_merged_count),
                    'write_merged': min(write_merged_count)}

        df=pd.DataFrame({'x': range(len(read_count)),
                        'read_count': read_count,
                        'write_count': write_count,
                        'read_bytes': read_bytes,
                        'write_bytes': write_bytes,
                        'read_time': read_time,
                        'write_time': write_time,
                        'busy_time': busy_time,
                        'read_merged': read_merged_count,
                        'write_merged': write_merged_count })

        # read_count = [ element - min_data['read_count'] for element in read_count]
        # write_count = [ element - min_data['write_count'] for element in write_count]
        # read_bytes = [ element - min_data['read_bytes'] for element in read_bytes]
        # write_bytes = [ element - min_data['write_bytes'] for element in write_bytes]
        # read_time = [ element - min_data['read_time'] for element in read_time]
        # write_time = [ element - min_data['write_time'] for element in write_time]
        # busy_time = [ element - min_data['busy_time'] for element in busy_time]
        # read_merged_count = [ element - min_data['read_merged_count'] for element in read_merged_count]
        # write_merged_count = [ element - min_data['write_merged_count'] for element in write_merged_count]

        # Initialize the figure style
        plt.style.use('seaborn')

        # create a color palette
        palette = plt.get_cmap('Set1')

        # multiple line plot
        num=0
        for column in df.drop('x', axis=1):
            num+=1

            # Find the right spot on the plot
            plt.subplot(3,3, num)
            plt.subplots_adjust(wspace=0.7,hspace = 0.4)
            # Plot the lineplot
            plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1.9, alpha=1, label=column)

            min_data_temp = int(float(min_data[column]))
            max_data_temp = int(float(max_data[column]))
            # Same limits for every chart
            plt.xlim(0,len(read_count)+1)
            plt.ylim(min_data_temp,max_data_temp)
            #plt.ticklabel_format(axis="y", style="sci", scilimits=(1,2), useOffset=False, useMathText=False)
            plt.ticklabel_format(axis='y',scilimits=(1,2), useOffset=False) #, useLocale=True,useMathText=False)

            # Not ticks everywhere
            if num in range(len(read_count)):
                plt.tick_params(labelbottom='off')
            if num not in df[column]:
                plt.tick_params(labelleft='off')

            # Add title
            plt.title(column, loc='right', fontsize=10, fontweight=1, color=palette(num) )

        program = path.split('/')[-3]
        # general title
        plt.suptitle("Disk IO Counters - "+program.upper(), fontsize=13, fontweight=0, color='black', style='italic')



        # Axis titles
        #plt.text(-1, +3146984, 'Tiempo', ha='left', va='top')

        iteration = path.split('/')[-2]
        #Show the graph
        plt.savefig("Plots/" + str(Estudio_Dir) + "/diskiocounters/" + program + "_" + iteration + "_" + 'diskiocounters_graph.png' ,bbox_inches='tight',pad_inches=0.5)
        plt.clf()
        plt.close('all')

def vmemory():
    os.system('mkdir -p Plots/' + str(Estudio_Dir) + '/vmemory')
    paths = find_all('vmemory.txt',Estudio_Dir)
    for path in paths:

        available = []
        used = []
        free = []
        active = []
        inactive = []
        buffers = []
        cached = []
        shared = []

        numrow = 0
        with open(path,'r') as data:
            for line in csv.reader(data):
                try:
                    available.append(float(line[0]))
                    used.append(float(line[1]))
                    free.append(float(line[2]))
                    active.append(float(line[3]))
                    inactive.append(float(line[4]))
                    buffers.append(float(line[5]))
                    cached.append(float(line[6]))
                    shared.append(float(line[7]))
                    numrow += 1
                except:
                    pass


        max_data = {'available': max(available),
                    'used': max(used),
                    'free': max(free),
                    'active': max(active),
                    'inactive': max(inactive),
                    'buffers': max(buffers),
                    'cached': max(cached),
                    'shared': max(shared)}

        min_data = {'available': min(available),
                    'used': min(used),
                    'free': min(free),
                    'active': min(active),
                    'inactive': min(inactive),
                    'buffers': min(buffers),
                    'cached': min(cached),
                    'shared': min(shared)}

        df=pd.DataFrame({'x': range(len(available)),
                        'available': available,
                        'used': used,
                        'free': free,
                        'active': active,
                        'inactive': inactive,
                        'buffers': buffers,
                        'cached': cached,
                        'shared': shared})

        # Initialize the figure style
        plt.style.use('seaborn')

        # create a color palette
        palette = plt.get_cmap('Set1')

        # multiple line plot
        num=0
        for column in df.drop('x', axis=1):
            num+=1

            # Find the right spot on the plot
            plt.subplot(4,2, num)
            plt.subplots_adjust(wspace=0.2,hspace = 0.4)
            # Plot the lineplot
            plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1, alpha=1, label=column)

            min_data_temp = int(float(min_data[column]))
            max_data_temp = int(float(max_data[column]))
            # Same limits for every chart
            plt.xlim(0,len(available)+1)
            plt.ylim(min_data_temp,max_data_temp)
            #plt.ticklabel_format(axis="y", style="sci", scilimits=(1,2), useOffset=False, useMathText=False)
            plt.ticklabel_format(axis='y',scilimits=(1,2), useOffset=False) #, useLocale=True,useMathText=False)

            # Not ticks everywhere
            if num in range(len(available)):
                plt.tick_params(labelbottom='off')
            if num not in df[column]:
                plt.tick_params(labelleft='off')

            # Add title
            plt.title(column, loc='right', fontsize=10, fontweight=1, color=palette(num) )

        program = path.split('/')[-3]
        # general title
        plt.suptitle("Virtual Memory - "+program.upper(), fontsize=13, fontweight=0, color='black', style='italic')



        # Axis titles
        #plt.text(-1, +3146984, 'Tiempo', ha='left', va='top')

        iteration = path.split('/')[-2]
        #Show the graph
        plt.savefig("Plots/" + str(Estudio_Dir) + "/vmemory/" + program + "_" + iteration + "_" + 'vmemory_graph.png' ,bbox_inches='tight',pad_inches=0.5)
        plt.clf()
        plt.close('all')

if __name__ == '__main__':
    cpufreq()
    cpupercent()
    cpustats()
    cputimes()
    diskiocounters()
    vmemory()
