answer = 'Y'
numeros = []
while answer == 'Y':
    numero = int(input('Type a number: '))
    if numero not in numeros:
        numeros.append(numero)
    while True:
        answer = str(input('Would you like to continue? (Y/N)')).strip().upper()
        if answer and answer[0] in 'YN':
            break
        print('Invalid Answer')
print(f'The unique numbers typed are: {sorted(numeros)}')
