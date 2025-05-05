qtd_pessoas = 0
pessoas = []
extra = []
pesadas = []
leves = []
resposta = 'S'
maior = menor = 0
while resposta == 'S':
    nome = (str(input('Digite o nome da pessoa: ')))
    qtd_pessoas += 1
    peso = (int(input('Digite o peso da pessoa: ')))
    extra.append(nome)
    extra.append(peso)
    pessoas.append(extra[:])
    extra.clear()
    resposta = str(input('Quer continuar?')).upper().strip()

    if maior == 0 or peso > maior:
        maior = peso
    if menor == 0 or peso < menor:
        menor = peso

for i in pessoas:
    if i[1] == maior:
        pesadas.append(i[0])
    if i[1] == menor:
        leves.append(i[0])
print(f'{qtd_pessoas} pessoas')
print(pesadas)
print(leves)

'''
pessoas = []

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

# Determina maior e menor peso
pesos = [p[1] for p in pessoas]
maior = max(pesos)
menor = min(pesos)

# Lista quem tem o maior e menor peso
pesadas = [p[0] for p in pessoas if p[1] == maior]
leves = [p[0] for p in pessoas if p[1] == menor]

print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')
print(f'Mais pesadas: {pesadas} com {maior}kg')
print(f'Mais leves: {leves} com {menor}kg')'''

