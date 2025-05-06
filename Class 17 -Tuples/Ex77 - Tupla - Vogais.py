palavras = ('Melancia', 'Parede', 'Cachorro', 'Manga')

for palavra in palavras:
    print('\n', palavra, '---', end=' ')
    for letra in palavra:

        if letra.lower() in 'aeiou':
            print(letra, end='')