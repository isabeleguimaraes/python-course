#EXERCICIO 43
'''peso = float(input('Digite seu peso em kilogramas: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print(f'Seu peso é {peso}, sua altura é {altura}, portanto seu IMC é {imc:.1f}.')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está com o peso ideal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está com obesidade')
else:
    print('Você está com Obesidade Mórbida. Cuidado.')'''

#EXERCICIO 44

'''preco_normal = float(input('Digite o preco do produto: '))
print(Metodos de Pagamento:
[1] - à vista em dinheiro ou cheque
[2] - à vista no cartão
[3] - em até 2x no cartão
[4] - em 3x ou mais no cartão)
opcao = int(input('Digite dentre as opções acima, qual o seu método de pagamento'))

if opcao == 1:
    print(f'O preço a pagar é de {preco_normal * 0.9}')
elif opcao == 2:
    print(f'O preço a pagar é de {preco_normal * 0.95}')
elif opcao == 3:
    print(f'O preço a pagar é de {preco_normal}')
elif opcao == 4:
    print(f'O preço a pagar é de {preco_normal * 1.2}')'''

#EXERCICIO 45

import random
lista = ['Pedra', 'Papel', 'Tesoura']
jogada_pc = random.choice(lista)
jogada_usuario = input('Escolha Pedra, Papel ou Tesoura ').capitalize().strip()
print(f'O computador jogou {jogada_pc} e você jogou {jogada_usuario}.')
if (jogada_pc == 'Pedra' and jogada_usuario == 'Papel'
    or jogada_pc == 'Tesoura' and jogada_usuario == 'Pedra'
    or jogada_pc == 'Papel' and jogada_usuario == 'Tesoura'):
    print('Você ganhou!')
elif (jogada_pc == 'Pedra' and jogada_usuario == 'Tesoura'
    or jogada_pc == 'Papel' and jogada_usuario == 'Pedra'
    or jogada_pc == 'Tesoura' and jogada_usuario == 'Papel'):
    print('Você perdeu!')
else:
    print('Você empatou!')





