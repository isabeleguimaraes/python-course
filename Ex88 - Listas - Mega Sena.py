from random import randint
from time import sleep
jogos = []
quantidade = int(input('Quantos jogos?'))

for jogo in range(0,quantidade):
    jogos.append([])
    while len(jogos[jogo]) < 6:
        numero = randint(1,60)
        if numero not in jogos[jogo]:
            jogos[jogo].append(numero)
    print(f'O jogo {jogo+1} é: {jogos[jogo]}')
    sleep(1)
print('Boa sorte!')
