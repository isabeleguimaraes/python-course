'''from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print(numeros)
print(f'O maior valor foi {max(numeros)} e o menor valor foi {min(numeros)}')'''

from random import randint

numeros = tuple(randint(1,10) for i in range (0,5))
print(numeros)
