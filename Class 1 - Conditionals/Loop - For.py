'''n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o segundo numero '))
n3 = int(input('Digite o terceiro numero '))
n4 = int(input('Digite o quarto numero' ))
n5 = int(input('Digite o quinto numero' ))
n6 = int(input('Digite o sexto numero '))


soma = 0
numeros = [n1, n2, n3, n4, n5, n6]

for numero in numeros:
    if numero % 2 == 0:
        soma += numero
print(soma)'''
'''soma = 0
for item in range(1,7):
    numero = int(input(f'Digite o {item}º numero: '))
    if numero % 2 == 0:
        soma += numero
print(soma)'''

###

'''primeiro = int(input('Qual o primeiro termo'))
razao = int(input('Qual a razao'))

for item in range(0,10):
   termo = primeiro + item * razao
   print(f'O termo {item+1} é {termo}')'''

### Numero Primo

'''numero = int(input('Digite um número inteiro: '))
count = 0
for item in range(1,numero+1):
    if numero % item == 0:
        count = count + 1
if count == 2:
    print('Esse numero é primo')
else:
    print('Esse numero nao é primo')'''




