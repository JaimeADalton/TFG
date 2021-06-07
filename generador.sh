#!/bin/bash

#installed_packages=$(apt list --installed | cut -d"/" -f 1)
#if [[ ! "libtext-lorem-perl" == $installed_packages ]];then
#echo installing libtext-lorem-perl
#sudo apt install libtext-lorem-perl
#fi
# filesize=10485760 #(10MiB)
# filesize=52428800  #(50MiB)
filesize=26214400  #(25MiB)

mkdir -p RawData

function text_generator {
	tr -dc a-z1-4 </dev/urandom | tr 1-2 ' \n' | awk 'length==0 || length>50' | tr 3-4 ' ' | sed 's/^ *//' | cat -s | sed 's/ / /g' |fmt |  head -c $filesize > RawData/texto_random_$1.txt
}

function lorem_ipsum {
	filename="RawData/texto_lorem_$1.txt"
	touch $filename
	touch tmp.txt
	size=0
	while [[ $size -lt $filesize ]]
	do
		num=$(python -c "from random import randint; print(randint(1,10000))")
		choise=$(python -c "from random import randint; print(randint(1,1))")
		times=$(python -c "from random import randint; print(randint(1,10))")
		for ((j=0;j<=$times;j++))
		do
			case $choise in
				1) echo -n " " && lorem -s $num >> tmp.txt;;
				2) echo -n " " && lorem -p $num >> tmp.txt;;
			esac
		done
		size=$(du -b tmp.txt | awk '{print $1}')
	done
	head -c $filesize tmp.txt > $filename
	rm tmp.txt
}

function ascii_generator {
	base64 /dev/urandom | head -c $filesize > RawData/texto_ascii_$1.txt
}

function check_file {
	case $1 in
		'1') if [[ -f "RawData/texto_random_1.txt" ]]; then last_num_file=$(ls RawData/texto_random*.txt| grep -Eo '[0-9]{1,3}' | sort -n | tail -n 1);else last_num_file=0;fi;;
		'2') if [[ -f "RawData/texto_lorem_1.txt" ]]; then last_num_file=$(ls RawData/texto_lorem*.txt | grep -Eo '[0-9]{1,3}' | sort -n | tail -n 1);else last_num_file=0;fi;;
		'3') if [[ -f "RawData/texto_ascii_1.txt" ]]; then last_num_file=$(ls RawData/texto_ascii*.txt | grep -Eo '[0-9]{1,3}' | sort -n | tail -n 1);else last_num_file=0;fi;;
	esac
	echo $(($last_num_file + 1))
}

function menu {
	echo "[1] Generador de texto aleatorio"
	echo "[2] Generador de texto lorem ipsum"
	echo "[3] Generador de texto ASCII"
	read -p "Elige una opcion [1|2|3]: " opcion
	num=$(check_file "$opcion")
	case $opcion in
		1)text_generator $num;;
		2)lorem_ipsum $num;; 
		3)ascii_generator $num;;
	esac
}

menu
