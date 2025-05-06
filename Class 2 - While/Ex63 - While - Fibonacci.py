n = int(input('Quantos numeros da sequência de Fibonacci você deseja ver? '))
termo1 = 0
termo2 = 1
c = 2
print(termo1,termo2, end=' ')
while c < n:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    c = c + 1
    print(termo3, end=' ')
print('\nFIM')


