import datetime
menores = 0
maiores = 0
ano_atual = datetime.date.today().year
for item in range(0,7):
    nasc = int(input('Digite um ano de nascimento: '))
    if  ano_atual - nasc < 18:
        menores += 1
    elif ano_atual - nasc >= 18:
        maiores += 1
print(maiores)
print(menores)
