#!/bin/bash


#Si no funciona asegurarse que los directorios Estudio_# no no tengan ningun subdirectorio que no sea
# 7z clzip gzip lzop pbzip2 pigz zip
mv TimeDuData.txt TimeDuData.txt.bkp
touch TimeDuData.txt
for ((estudio=1;estudio<=8;estudio++))
do
    dir="Estudio_$estudio"
    echo $dir
    if [[ ! -d $dir ]];then break; fi
    ls_program=($(find $dir -maxdepth 1 -type d))
    for pro in {1..7}
    do
        program=${ls_program[pro]}
        subdir_programs=($(find $program -type d))
        length=$(echo ${subdir_programs[@]} | sed 's/\ /\n/g' | wc -l) 
        for (( j=1; j< $length; j++ ));do
            program_name=$(echo ${subdir_programs[$j]} | cut -d/ -f 2)
            if [[ $program_name == "Plots" ]];then 
                continue
            else
                iteration=$(echo ${subdir_programs[$j]} | cut -d/ -f 3)
                du_file=${subdir_programs[$j]}/*.du
                time_file=${subdir_programs[$j]}/*.time
                bytes=$(cat $du_file | cut -d"R" -f1)
                user=$(cat $time_file | head -n 1 | cut -d" " -f1 | sed 's/user//g')
                system=$(cat $time_file | head -n 1 | cut -d" " -f2 | sed 's/system//g')
                elapsed=$(cat $time_file | head -n 1 | cut -d" " -f3 | sed 's/elapsed//g')
                CPU=$(cat $time_file | head -n 1 | cut -d" " -f4 | sed 's/\%CPU//g')
                echo $estudio, $program_name, $iteration, $bytes, $user, $system, $elapsed, $CPU >> TimeDuData.txt
            fi
        done
    done
done