numeros = []
maior = None
menor = None
for i in range(0,5):
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    if maior is None or valor > maior:
        maior = valor
    if menor is None or valor < menor:
        menor = valor
print(f'A lista criada é {numeros}')
print(f'O maior número é o {maior}, na posição', end=' ')
for pos, num in enumerate(numeros):
    if num == maior:
        print(pos, end=', ')
print(f'\nO menor número é {menor}, na posição', end=' ')
for pos, num in enumerate(numeros):
    if num == menor:
        print(pos, end=',')



