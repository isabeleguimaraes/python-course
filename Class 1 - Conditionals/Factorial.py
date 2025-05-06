'''numero = int(input('Digite numero'))
fatorial = 1

for item in range(1, numero+1):
    fatorial = fatorial * item
print(fatorial)'''

n = int(input('Digite um numero'))
f = 1

while n > 0:
    f = f * n
    n = n - 1
print(f)