soma = quantidade = 0
barato = None

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preço do produto: '))
    soma += preco
    if preco > 1000:
        quantidade += 1
    if barato is None or preco < barato:
        barato = preco
        nomebarato = nome
    while True:
        resposta = str(input('Deseja adicionar mais produtos? (S/N)')).upper().strip()
        if resposta and resposta[0] in ('S', 'N'):
            break
        print('Resposta inválida. Por favor digite Sim ou Não.')
    if resposta[0] == 'N':
        break
print(f'O total da sua compra foi de ${soma}, com {quantidade} produtos acima de $1000, e {nomebarato} foi o produto mais barato custando {barato}' reais.)