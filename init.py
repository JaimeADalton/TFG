#!/usr/bin/python3
import os
import threading
import time

def Counter():
    counter = open('counter.txt', 'r')
    count = int(counter.read())
    counter.close()
    return count

def CounterAdd():
    counter = Counter()
    file = open('counter.txt', 'w+')
    counter = counter + 1
    print(str(counter), file=file)
    file.close()

def Start_Compress():
    counter = open('counter.txt', 'r')
    count = int(counter.read())
    counter.close()
    print(count, "Iteracion Init")
    if count == 1:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=3 -md=8m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 2:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=3 -md=16m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 3:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=3 -md=32m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 4:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=3 -md=64m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 5:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=5 -md=8m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 6:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=5 -md=16m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 7:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=5 -md=32m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 8:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=5 -md=64m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 9:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=9 -md=8m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 10:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=9 -md=16m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 11:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=9 -md=32m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 12:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma -mx=9 -md=64m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 13:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=3 -md=8m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 14:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=3 -md=16m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 15:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=3 -md=32m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 16:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=3 -md=64m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 17:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=5 -md=8m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 18:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=5 -md=16m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 19:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=5 -md=32m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 20:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=5 -md=64m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 21:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=9 -md=8m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 22:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=9 -md=16m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 23:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=9 -md=32m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 24:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=lzma2 -mx=9 -md=64m RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 25:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=deflate -mx=3 RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 26:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=deflate -mx=5 RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 27:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=deflate -mx=9 RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 28:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=deflate64 -mx=3 RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 29:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=deflate64 -mx=5 RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 30:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=deflate64 -mx=9 RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 31:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=ppmd -mx=3 RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 32:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=ppmd -mx=5 RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 33:
        time.sleep(0.5)
        os.system('{ time 7z a -t7z -m0=ppmd -mx=9 RawData/7zip'+str(count)+'.7z RawData/data.txt ; } 2> Datos/7z/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/7zip'+str(count)+'.7z > Datos/7z/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 34:
        time.sleep(0.5)
        os.system('{ time clzip -k -3 --dictionary-size=2MiB  RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 35:
        time.sleep(0.5)
        os.system('{ time clzip -k -3 --dictionary-size=4MiB  RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 36:
        time.sleep(0.5)
        os.system('{ time clzip -k -3 --dictionary-size=8MiB  RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 37:
        time.sleep(0.5)
        os.system('{ time clzip -k -3 --dictionary-size=16MiB  RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 38:
        time.sleep(0.5)
        os.system('{ time clzip -k -3 --dictionary-size=32MiB  RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 39:
        time.sleep(0.5)
        os.system('{ time clzip -k -6 --dictionary-size=2MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 40:
        time.sleep(0.5)
        os.system('{ time clzip -k -6 --dictionary-size=4MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 41:
        time.sleep(0.5)
        os.system('{ time clzip -k -6 --dictionary-size=8MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 42:
        time.sleep(0.5)
        os.system('{ time clzip -k -6 --dictionary-size=16MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 43:
        time.sleep(0.5)
        os.system('{ time clzip -k -6 --dictionary-size=32MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 44:
        time.sleep(0.5)
        os.system('{ time clzip -k -9 --dictionary-size=2MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 45:
        time.sleep(0.5)
        os.system('{ time clzip -k -9 --dictionary-size=4MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 46:
        time.sleep(0.5)
        os.system('{ time clzip -k -9 --dictionary-size=8MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 47:
        time.sleep(0.5)
        os.system('{ time clzip -k -9 --dictionary-size=16MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 48:
        time.sleep(0.5)
        os.system('{ time clzip -k -9 --dictionary-size=32MiB   RawData/data.txt -o RawData/data.txt.lz ; } 2> Datos/clzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lz > Datos/clzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 49:
        time.sleep(0.5)
        os.system('{ time gzip -3 -c RawData/data.txt > RawData/data.txt'+str(count)+'.gz ; } 2> Datos/gzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.gz > Datos/gzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 50:
        time.sleep(0.5)
        os.system('{ time gzip -6 -c RawData/data.txt > RawData/data.txt'+str(count)+'.gz ; } 2> Datos/gzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.gz > Datos/gzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 51:
        time.sleep(0.5)
        os.system('{ time gzip -9 -c RawData/data.txt > RawData/data.txt'+str(count)+'.gz ; } 2> Datos/gzip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.gz > Datos/gzip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 52:
        time.sleep(0.5)
        os.system('{ time lzop -3 RawData/data.txt -o RawData/data.txt.lzo ; } 2> Datos/lzop/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lzo > Datos/lzop/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *o')
        time.sleep(0.5)
        os.system('')

    if count == 53:
        time.sleep(0.5)
        os.system('{ time lzop -5 RawData/data.txt -o RawData/data.txt.lzo ; } 2> Datos/lzop/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lzo > Datos/lzop/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *o')
        time.sleep(0.5)
        os.system('')

    if count == 54:
        time.sleep(0.5)
        os.system('{ time lzop -7 RawData/data.txt -o RawData/data.txt.lzo ; } 2> Datos/lzop/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lzo > Datos/lzop/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *o')
        time.sleep(0.5)
        os.system('')

    if count == 55:
        time.sleep(0.5)
        os.system('{ time lzop -9 RawData/data.txt -o RawData/data.txt.lzo ; } 2> Datos/lzop/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.lzo > Datos/lzop/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *o')
        time.sleep(0.5)
        os.system('')

    if count == 56:
        time.sleep(0.5)
        os.system('{ time pbzip2 -3 -c < RawData/data.txt > RawData/data.txt'+str(count)+'.bz2 ; } 2> Datos/pbzip2/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.bz2 > Datos/pbzip2/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *2')
        time.sleep(0.5)
        os.system('')

    if count == 57:
        time.sleep(0.5)
        os.system('{ time pbzip2 -5 -c < RawData/data.txt > RawData/data.txt'+str(count)+'.bz2 ; } 2> Datos/pbzip2/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.bz2 > Datos/pbzip2/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *2')
        time.sleep(0.5)
        os.system('')

    if count == 58:
        time.sleep(0.5)
        os.system('{ time pbzip2 -9 -c < RawData/data.txt > RawData/data.txt'+str(count)+'.bz2 ; } 2> Datos/pbzip2/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.bz2 > Datos/pbzip2/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *2')
        time.sleep(0.5)
        os.system('')

    if count == 59:
        time.sleep(0.5)
        os.system('{ time pigz -3 -k -f RawData/data.txt ; } 2> Datos/pigz/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.gz > Datos/pigz/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 60:
        time.sleep(0.5)
        os.system('{ time pigz -5 -k -f RawData/data.txt ; } 2> Datos/pigz/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.gz > Datos/pigz/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 61:
        time.sleep(0.5)
        os.system('{ time pigz -7 -k -f RawData/data.txt ; } 2> Datos/pigz/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.gz > Datos/pigz/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 62:
        time.sleep(0.5)
        os.system('{ time pigz -9 -k -f RawData/data.txt ; } 2> Datos/pigz/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt.gz > Datos/pigz/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *z')
        time.sleep(0.5)
        os.system('')

    if count == 63:
        time.sleep(0.5)
        os.system('{ time zip -3 RawData/data.txt'+str(count)+'.zip RawData/data.txt; } 2> Datos/zip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.zip > Datos/zip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *p')
        time.sleep(0.5)
        os.system('')

    if count == 64:
        time.sleep(0.5)
        os.system('{ time zip -5 RawData/data.txt'+str(count)+'.zip RawData/data.txt; } 2> Datos/zip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.zip > Datos/zip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *p')
        time.sleep(0.5)
        os.system('')

    if count == 65:
        time.sleep(0.5)
        os.system('{ time zip -7 RawData/data.txt'+str(count)+'.zip RawData/data.txt; } 2> Datos/zip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.zip > Datos/zip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *p')
        time.sleep(0.5)
        os.system('')

    if count == 66:
        time.sleep(0.5)
        os.system('{ time zip -9 RawData/data.txt'+str(count)+'.zip RawData/data.txt; } 2> Datos/zip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.zip > Datos/zip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *p')
        time.sleep(0.5)
        os.system('')

    if count == 67:
        time.sleep(0.5)
        os.system('{ time zip -Z bzip2 -3 RawData/data.txt'+str(count)+'.zip RawData/data.txt; } 2> Datos/zip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.zip > Datos/zip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *p')
        time.sleep(0.5)
        os.system('')

    if count == 68:
        time.sleep(0.5)
        os.system('{ time zip -Z bzip2 -5 RawData/data.txt'+str(count)+'.zip RawData/data.txt; } 2> Datos/zip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.zip > Datos/zip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *p')
        time.sleep(0.5)
        os.system('')

    if count == 69:
        time.sleep(0.5)
        os.system('{ time zip -Z bzip2 -7 RawData/data.txt'+str(count)+'.zip RawData/data.txt; } 2> Datos/zip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.zip > Datos/zip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *p')
        time.sleep(0.5)
        os.system('')

    if count == 70:
        time.sleep(0.5)
        os.system('{ time zip -Z bzip2 -9 RawData/data.txt'+str(count)+'.zip RawData/data.txt; } 2> Datos/zip/'+str(count)+'/'+str(count)+'.time')
        time.sleep(0.5)
        os.system('du -b RawData/data.txt'+str(count)+'.zip > Datos/zip/'+str(count)+'/'+str(count)+'.du')
        time.sleep(0.5)
        os.system('cd RawData/;rm *p')
        time.sleep(0.5)
        os.system('')

    CounterAdd()


def StartCollector():
    number = Counter()
    if 1 <= number <= 33:
        Name = '7z'
    if 34 <= number <= 48 :
        Name = 'clzip'
    if 49 <= number <= 51:
        Name = 'gzip'
    if 52 <= number <= 55:
        Name = 'lzop'
    if 56 <= number <= 58:
        Name = 'pbzip2'
    if 59 <= number <= 62:
        Name = 'pigz'
    if 63 <= number <= 70:
        Name = 'zip'
    os.system('/usr/bin/python3 DataColector.py ' + Name + ' ' + str(number))

for estudio in range(8):
    os.system('echo 1 > counter.txt')
    print("Estudio " + str(estudio))
    if estudio == 0:
        os.system('mv RawData/texto_lorem_1.txt RawData/data.txt')
    if estudio == 1:
        os.system('mv RawData/texto_ascii_1.txt RawData/data.txt')
    if estudio == 2:
        os.system('mv RawData/texto_random_1.txt RawData/data.txt')
    if estudio == 3:
        os.system('mv RawData/pdf.pdf RawData/data.txt')
    if estudio == 4:
        os.system('mv RawData/database.xml RawData/data.txt')
    if estudio == 5:
        os.system('mv RawData/lorem.docx RawData/data.txt')
    if estudio == 6:
        os.system('mv RawData/ascii.docx RawData/data.txt')
    if estudio == 7:
        os.system('mv RawData/random.docx RawData/data.txt')
    for iteracion in range(70):
        print("Iteracion " + str(iteracion))
        threading.Thread(target=StartCollector).start()
        time.sleep(0.5)
        threading.Thread(target=Start_Compress).start()
        time.sleep(60)
    if estudio == 0:
        os.system('mv Datos/ Estudio_1')
    if estudio == 1:
        os.system('mv Datos/ Estudio_2')
    if estudio == 2:
        os.system('mv Datos/ Estudio_3')
    if estudio == 3:
        os.system('mv Datos/ Estudio_4')
    if estudio == 4:
        os.system('mv Datos/ Estudio_5')
    if estudio == 5:
        os.system('mv Datos/ Estudio_6')
    if estudio == 6:
        os.system('mv Datos/ Estudio_7')
    if estudio == 7:
        os.system('mv Datos/ Estudio_8')

os.system('python init_graph.py')
