valor = int(input('Digite o valor a ser sacado: '))
valores = [50,20,10,1]

for cedula in valores:
    qtd = valor // cedula
    valor = valor % cedula
    print(f'{qtd} X {cedula}')
    if valor == 0:
        break
print('Obrigado, volte sempre!')