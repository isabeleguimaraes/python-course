expression = str(input('Digite uma expressão matemática: '))
pilha = []

for i in expression:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if pilha:
            pilha.pop()
        else:
            pilha.append(')')
            break
if pilha:
    print('Expressao invalida')
else:
    print('Expressao valida')

