lista = []
answer = 'Y'
while answer == 'Y':
    valor = int(input('Type a number: '))
    lista.append(valor)
    while True:
        answer = str(input('Quer continuar? (Y/N)')).upper().strip()
        if answer and answer[0] in 'YN':
            break
        print('Resposta inválida.')

lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números, que são: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 não foi digitado, portanto não está na lista.')


