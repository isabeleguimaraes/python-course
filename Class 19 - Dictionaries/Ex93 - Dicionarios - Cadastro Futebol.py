futebol = {}
totgols = 0
gols = []
futebol['nome'] = str(input('Digite o Nome do Jogador: '))
partidas = futebol['partidas'] = int(input('Digite quantas partidas ele jogou: '))

for i in range(1,partidas+1):
    num_gols = int(input(f'Partida {i}: Quantos gols? '))
    gols.append(num_gols)
    futebol['gols'] = gols
    totgols += num_gols
    futebol['totgols'] = totgols

print(futebol)

