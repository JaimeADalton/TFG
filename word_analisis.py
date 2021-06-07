#!/usr/bin/env python
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

def freq(str):
    str_list = str.split()
    unique_words = set(str_list)

    for words in unique_words :
        s = str_list.count(words)
        if s >  1:
            print(s, words )

if __name__ == "__main__":
    f = open(file_path , 'r')
    print(file_path.split('/')[-1])

    str=' '.join(' '.join(f.read().split('\n')).split('.'))

    freq(str)
