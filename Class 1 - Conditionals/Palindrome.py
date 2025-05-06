frase = input('Digite a frase').strip().lower().replace(' ','')
inverso = ''
for letra in range(len(frase) - 1, -1 ,-1):
    inverso = inverso + frase[letra]
if inverso == frase:
    print('Palindromo')
else:
    print('nao')



