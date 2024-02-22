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
import os

__version__ = "0.0.1"


cl=clfilter("crnm:", doc=__doc__)

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
        imprime(sorted(ocorr.items(), key=lambda x: x[0]))
    elif "-c" in cl.opt:
        deleted = []
        for x in ocorr:
            if x[0].isupper():
                lower = x.lower()
                if lower in ocorr:
                    if ocorr[x] > ocorr[lower]:
                        ocorr[x] += ocorr[lower]
                        deleted.append(lower)
                    else: 
                        ocorr[lower] += ocorr[x]
                        deleted.append(x)
        for x in deleted:
            ocorr.pop(x)
        imprime(ocorr.items())
    elif "-r" in cl.opt:
        file_path = os.path.join(os.path.dirname(__file__), 'dataPT', 'tabelas_ocorencias.txt')
        f =open(file_path, "r", encoding="iso-8859-1")
        ocorr_tabela = {}
        for line in f:
            parts = line.split('\t')
            if len(parts) == 2:
                number, word = parts
                word = word.strip()
                if word.isalpha(): 
                    ocorr_tabela[word] = int(number)
        
        deleted = []        
        for x in ocorr:
            if x in ocorr_tabela:
                num_ocorr = ocorr[x]
                ocorr[x] = num_ocorr / ocorr_tabela[x]
            else:
                deleted.append(x)
        for x in deleted:
            ocorr.pop(x)
        ocorr_ordenado = dict(sorted(ocorr.items(), key=lambda item: item[1], reverse=True))
        imprime(ocorr_ordenado.items())
    else:
        print("Wrong Option")   
    print("\n\n")  

