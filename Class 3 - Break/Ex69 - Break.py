maioridade = 0
homens = 0
mulher_menor = 0
while True:
    idade = int(input('Qual a idade da pessoa?'))
    while True:
        sexo =  str(input('Qual o sexo da pessoa? (M/F)')).upper().strip()
        if sexo and sexo[0] in ('M', 'F'):
            break
        print('Resposta Inválida. Por favor digite M ou F')
    while True:
        resposta = str(input('Quer continuar? (S/N)')).upper().strip()[0]
        if resposta in ('S','N'):
            break
        print('Resposta inválida. Por favor digite S ou N')
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    if resposta == 'N':
        break
print(f'Foram cadastrados {maioridade} pessoas com maior de 18 anos, {homens} homens e {mulher_menor} mulheres com menos de 20 anos')
