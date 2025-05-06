from random import randint
from operator import itemgetter
from time import sleep
jogo = {}
ranking = {}

for d in range(1,5):
    jogo[f'Jogador {d}'] = randint(1,6)
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)

#Ordenar um dicionário: precisa criar um outro dicionário e ativar o import operator/itemgetter

# jogo.items() é uma tupla (junta a key e o value). sorted() forma uma lista, logo, o retorno dessa expressão
# será uma lista de tuplas. O key=itemgetter(1) é para ordenador pelo value, ja que no automatico será pela key.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print('Ranking dos Jogadores')

for i, v in enumerate(ranking):
    print(f' {i+1} lugar: {v[0]} = {v[1]}')
    sleep(0.5)



