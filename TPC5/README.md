In TPC5, a list of tokens, read from the input file, is processed in order to determine their POS and Lemma. This processing is carried out with the help of the spaCy library. Furthermore, entities (locations, names, ...) must have priority over other tokens.

Commands to execute:
```pip install -U spacy
python -m spacy download en_core_new
python3 spacy_proj.py [input_file]
```

Output:
```
  Palavra   |  POS  |   Lema 
_____________________________
O  DET  o
Daniel  PER  Daniel
e  CCONJ  e
o  DET  o
André  ORG  André
foram  AUX  ser
a  DET  o
Ponte de Lima  LOC  Ponte de Lima
a  ADP  a
pé  NOUN  pé
.  PUNCT  .

  SPACE  
```
