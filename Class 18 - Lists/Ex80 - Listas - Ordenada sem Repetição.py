lista = []
for resposta in range(0,5):
    valor = int(input('Type a number: '))
    if valor not in lista:
        if not lista or valor > lista[-1]:
            lista.append(valor)
        else:
            for item in range(0, len(lista)):
                if valor < lista[item]:
                    lista.insert(item,valor)
                    break
print(lista)