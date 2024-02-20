#!/usr/bin/env python3
'''
NAME
   word_freq - Calculates word frequency in a text

SYNOPSIS
   word_freq [options] input_files
   options: 
        -m 20 : Show 20 most common
        -n : Order alfabetically
Description'''

from jjcli import * 
from collections import Counter
import re


cl=clfilter("nm:", doc=__doc__)

def tokens(texto):
    words = re.findall(r'\w+(?:\-\w+)?|[,;.:_?!—]+', texto)
    return words

def imprime(list):
    for palavra, ocorr in list:
        print(palavra + " -> " + str(ocorr))

for txt in cl.text():   
    words_list = tokens(txt)
    ocorr = Counter(words_list)
    
    if "-m" in cl.opt:
        imprime(ocorr.most_common(int(cl.opt.get("-m"))))
    elif "-n" in cl.opt:
        imprime(ocorr.items())
    else:
        print("Wrong Option")     



