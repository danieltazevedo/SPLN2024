TPC6 aims to find the best friends in the book Harry Potter and the Philosopher's Stone. To achieve this objective, the spacy module is used to find all the names, sentence by sentence, if there are two different names in the same sentence, these characters are friends, Therefore, a count of pairs of characters that appear in the same sentence is carried out.

Commands to execute:
```pip install -U spacy
python -m spacy download en_core_new
python3 friends_proj.py [input_file]
```

Output from 5 best friends:
```
Melhores amigos:
('Harry', 'Ron') : 296
('Harry', 'Hermione') : 168
('Hagrid', 'Harry') : 160
('Hermione', 'Ron') : 150
('Harry', 'Potter') : 110

```
