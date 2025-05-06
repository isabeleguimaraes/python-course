from random import randint
while True:
    while True:
        escolha = input('Par ou impar? (P/I)').upper().strip()[0]
        if escolha in ('P','I'):
            break


    numero = int(input('Digite seu número: '))
    pc = randint(1, 10)
    resultado = pc + numero
    print(f'Você escolheu {numero} e o computador escolheu {pc}, o resultado foi: {resultado}')
    if resultado % 2 == 0:
        tipo = 'P'
    else:
        tipo = 'I'

    if escolha == tipo:
        print('Você venceu! Jogue novamente.')
    else:
        print('Você perdeu!')
        break
print('Fim do jogo.')
