boletim = {}

boletim['nome'] = str(input('Nome do Aluno: '))
boletim['media'] = float(input('Média do Aluno: '))
if boletim['media'] >= 7:
    boletim['status'] = 'Aprovado'
elif 5 < boletim['media'] < 7:
    boletim['status'] = 'Recuperação'
else:
    boletim['status'] = 'Reprovado'

for k, v in boletim.items():
    print(f'{k} = {v}')
print(f'A média de {boletim['nome']} é {boletim['media']}, e ele está {boletim['status']}')