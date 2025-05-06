total = 0
count = 0
while True:
    x = int(input('Digite qualquer número'))
    if x == 999:
        break
    total += x
    count += 1

print(f'Você digitou {count} números, e a soma entre eles foi {total}')