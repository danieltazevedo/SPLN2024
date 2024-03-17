# pip install -U spacy
# python -m spacy download en_core_news_sm
import spacy
import sys

'''
NAME
   spacy_project - descreve o tipo e o lema de cada palavra presente no ficheiro de input

SYNOPSIS
   python3 spacy_project.py input_file
'''

# Load Portuguese language model
nlp = spacy.load("pt_core_news_lg")

input_file = open(sys.argv[1],'r')
data = input_file.read()

doc = nlp(data)
   

#tokens_sintaxe = []  
#for token in doc.ents:
#   token_split = str(token).split(" ")
#   data = (token,token_split,token.label_,token.lemma_)
#   tokens_sintaxe.append(data)

def verifica (tokens,token_split,indice,tamanho):
   r = True
   for i in range(indice,indice+tamanho):
      if i < len(tokens):
         if str(tokens[i][0]) not in token_split:
            r = False
      else:
         r = False
   return r
      
   
tokens = []
for token in doc:
   data = (token,token.pos_,token.lemma_)
   tokens.append(data)
   
for token in doc.ents:
   token_split = str(token).split(" ")
   tamanho = len(token_split)
   indices = []
   for i in range(0,len(tokens)):
      if verifica(tokens,token_split,i,tamanho): #cerificar se token especial esta em token
         indices.append(i)
   for i in indices:
      for j in range(0,tamanho):
         tokens.pop(i)
      data=(token,token.label_,token.lemma_)
      tokens.insert(i,data)

output = open("output",'w')
top = "  Palavra   |  POS  |   Lema \n_____________________________\n"
print(top)
output.write(top)

for token in tokens:
   data = f'''{token[0]}  {token[1]}  {token[2]}\n'''
   print(data)
   output.write(data)

output.close()
       