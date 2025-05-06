n = 1
p = 0
i = 0
while n != 0:
    n = int(input('Digite valor'))
    if n!= 0:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1
print('Acabou')
print(i)
print(p)