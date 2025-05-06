programa = True
menu = True
while programa:
    numero1 = int(input('Digite um numero'))
    numero2 = int(input('Digite outro numero'))
    menu = True
    while menu:
        print('''Menu:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior Numero
        [ 4 ] Novos Numeros
        [ 5 ] Sair do Programa ''')
        escolha = int(input('Qual é a sua opção?'))
        if escolha == 1:
            print(f'A soma dos numeros é {numero1 + numero2}')
        elif escolha == 2:
            print(f'A multiplicação dos numeros é {numero1 * numero2}')
        elif escolha == 3:
            if numero1 > numero2:
                print(f'O {numero1} é maior')
            elif numero2 > numero1:
                print(f'O {numero2} é maior')
            else:
                print('Eles sao iguais')
        elif escolha == 4:
            menu = False
        elif escolha == 5:
            menu = False
            programa = False
print('Acabou')






