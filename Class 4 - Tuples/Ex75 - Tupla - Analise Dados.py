numeros = tuple(int(input('Digite um numero')) for i in range(4))
print(numeros)

print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na posição {numeros.index(3)+1}')
else:
    print('Não tem número 3.')

print(f'Os números pares são:', end='')
for item in numeros:
    if item % 2 == 0:
        print(item, end=',')
