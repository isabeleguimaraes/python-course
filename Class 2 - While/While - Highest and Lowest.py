pesos = []

for item in range(5):
    peso = int(input('Digite o peso: '))
    pesos.append(peso)

print(max(pesos))
print(min(pesos))

'''or'''

'''
maior = 0
menor = 0

for p in range(5):
    peso = float(input('Digite o Peso'))
    if p == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

'''

