total = 0
velho = 0
count = 0
nome_velho = ''
for i in range(1,5):
    nome = (input('Nome'))
    idade = int(input('Idade'))
    sexo = input('Sexo')
    total = total + idade
    if sexo == 'M' and idade > velho:
            velho = idade
            nome_velho = nome
    if sexo == 'F' and idade < 20:
        count = count + 1
media = total / 4
print(media)
print(count)
print(nome_velho)


