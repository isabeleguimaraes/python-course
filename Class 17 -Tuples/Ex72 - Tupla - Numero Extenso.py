numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    usuario = int(input('Digite um número de 0 a 20: '))
    if usuario in range(0,21):
        break
    print('Número Inválido.')
print(numeros[usuario])
