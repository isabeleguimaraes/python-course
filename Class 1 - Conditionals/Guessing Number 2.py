from random import randint
computador = randint(0,10)
palpites = 0
errou = True

while errou:
    jogador = int(input('Digite um numero de 0 a 10'))
    palpites += 1
    if jogador == computador:
        errou = False
    elif jogador < computador:
        print('Mais..')
    elif jogador > computador:
        print('Menos..')
print('Acertou!')
print(palpites)