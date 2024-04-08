import spacy
import itertools
import sys

nlp = spacy.load("pt_core_news_lg")

file = open(sys.argv[1],'r')
data = file.read()

doc = nlp(data)
amigos = {}

#ciclo for em todas as frases
for sent in doc.sents:
    nomes = []
    for token in sent: #para cada palavra verificar se é um nome
        if token.pos_=="PROPN":
            nomes.append(token.text)
    for nome1 in nomes:
        for nome2 in nomes:
            if nome1 != nome2:
                amizade = tuple(sorted([nome1, nome2]))
                if amizade in amigos:
                    amigos[amizade] +=1
                else:
                    amigos[amizade] =1

amigos = sorted(amigos.items(), key=lambda x: x[1], reverse=True)

print("Melhores amigos:")
for chave, valor in itertools.islice(amigos, 5):
    print(f"{chave} : {valor}")

output = open("output.txt",'w')
for chave, valor in amigos:
    output.write( f"{chave} : {valor}\n" )

file.close()
output.close()
