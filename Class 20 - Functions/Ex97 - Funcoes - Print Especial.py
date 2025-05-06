def titulo (a):
    medida = len(a) + 2
    print('~' * medida)
    print(f'{a:^{medida}}')
    print('~' * medida)

#Programa Principal
titulo('Bem-vindo')
titulo('Unidos da Tijuca')
