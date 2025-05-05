lista = [[],[],[]]
soma = 0
somac = 0

for l in range(0,3):
    for c in range (0,3):
        valor = int(input('Digite numero'))
        lista[l].append(valor)

for l in range(0,3):
    for c in range(0,3):
        print(f'{lista[l][c]:5}', end=' ')
    print()

for item in lista:
    for i in item:
        if i % 2 == 0:
            soma += i

for c in range(0,len(lista)):
    valor= (lista[c][2])
    somac += valor

maior = max(lista[1])

print(f'A soma de todos os valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é {maior}')
