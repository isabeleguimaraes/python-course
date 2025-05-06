mercado = ('Maçã', 'Banana', 'Uva', 'Melancia', 'Pêra', 4, 10, 3, 8, 9)
divisao = (len(mercado) // 2)
for item in range(divisao):
    print(mercado[item], '---', mercado[divisao+item])

listagem = ('Borracha', 1, 'Caneta', 2, 'Estojo', 5)
for item in range(0,len(listagem),2):
    print(listagem[item], '---', listagem[item+1])
