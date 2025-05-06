from random import randint

def sorteia(lista):
    for number in range(0,5):
        lista.append(randint(1,60))
    print(f'Os números sorteados foram: {lista}')


def somaPar(lista):
    soma = 0
    for number in lista:
        if number % 2 == 0:
            soma += number
    print(f'A soma dos numeros pares sorteados é: {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)