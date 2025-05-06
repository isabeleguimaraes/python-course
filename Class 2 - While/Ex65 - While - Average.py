count = soma = 0
resposta = 'S'
maior = menor = None

while True:
    numero = int(input('Digite um valor: '))
    count += 1
    soma += numero
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
         menor = numero
    resposta = input('Você deseja continuar? (S/N)').upper().strip()[0]
    if resposta == 'N':
        break
media = soma / count
print(f'A média dos valores digitados é {media}, o menor valor é {menor}, e o maior valor é {maior}')
