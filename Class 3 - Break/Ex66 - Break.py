quantidade = 0
soma = 0

while True:
    numero = int(input('Me diz um número qualquer inteiro, e digite 999 quando quiser parar.'))
    if numero == 999:
        break
    quantidade += 1
    soma += numero
print(f'A quantidade de números digitados foi {quantidade} e a soma deles foi {soma}')
