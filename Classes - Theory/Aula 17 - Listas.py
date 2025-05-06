valores = [1,2,3]
valores.append(5)
valores.append(1)
valores.sort()
valores.remove(3)
valores.pop()
valores.insert(0,9)
valores.sort()
for count, valor in enumerate(valores):
    print(valor)

print(valores)