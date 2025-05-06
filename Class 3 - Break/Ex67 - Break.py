while True:
    numero = int(input('Digite um número para ver a sua tabuada: '))
    if numero <= 0:
        break
    for item in range(1,11):
        print(f'{item}x{numero} = {item * numero}')
print('Programa encerrado!')