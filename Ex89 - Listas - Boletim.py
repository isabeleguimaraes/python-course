'''notas = []
temp = []
media = 0
while True:
    temp.append(str(input('Digite o Nome do Aluno')))
    temp.append(int(input('Digite a Nota 1 do Aluno')))
    temp.append(int(input('Digite a Nota 2 do Aluno')))
    notas.append(temp[:])
    temp.clear()
    resposta = str(input('Quer continuar? (S/N)')).upper().strip()
    if resposta == 'N':
        break
print(f'{'No.':^10}{'Aluno':^10}{'Media':^10}')
for no, aluno in enumerate(notas):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{no:^10}{aluno[0]:^10}{media:^10}')

numero = int(input('Se quiser ver as notas de um aluno específico, digite seu número correspondente.'))
print(f'As notas de {notas[numero][0]} foram {notas[numero][1]} e {notas[numero][2]} ')'''

notas = []
temp = []
media = 0
while True:
    nome = (str(input('Digite o Nome do Aluno')))
    nota1 = (int(input('Digite a Nota 1 do Aluno')))
    nota2 = (int(input('Digite a Nota 2 do Aluno')))
    notas.append([nome, nota1, nota2])
    resposta = str(input('Quer continuar? (S/N)')).upper().strip()
    if resposta == 'N':
        break
print(f'{'No.':^10}{'Aluno':^10}{'Media':^10}')
for no, aluno in enumerate(notas):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{no:^10}{aluno[0]:^10}{media:^10}')

numero = int(input('Se quiser ver as notas de um aluno específico, digite seu número correspondente.'))
print(f'As notas de {notas[numero][0]} foram {notas[numero][1]} e {notas[numero][2]} ')




