termo = int(input('Digite o primeiro termo '))
razao = int(input('Digite a razão '))
n = 1
total = 10
while True:
    while n <= total:
        ptermo = termo + (n-1) * razao
        print(ptermo)
        n = n + 1
    mais = int(input('Quantas vezes mais'))
    total = total + mais
    if mais == 0:
        break

