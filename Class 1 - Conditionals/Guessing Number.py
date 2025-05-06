from random import randint

npc = randint(0,10)
numero = int(input('Digite um valor de 0 a 10 para acertar: '))
count = 1

while npc != numero:
    if numero > npc:
        numero = int(input('Errou. Tente um numero menor!'))
    else:
        numero =  int(input('Errou. Tente um numero maior!'))
    count = count + 1
print('Você acertou!')
print(count)