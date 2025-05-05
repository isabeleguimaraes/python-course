dados = dict()
dados2 = {'nome': 'Pedro', 'idade': 25}
dados2['sexo'] = 'M'
del dados2['idade']

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

print(filme.values()) #Imprime os valores Star Wars, 1977, George Lucas
print(filme.keys()) #Imprime as categorias: titulo, ano, diretor
print(filme.items()) #Imprime o conjunto do value + key

#Keys e Values que nem o enumerate
for k, v in filme.items():
    print(f'O {k} é {v}')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome']) #Imprime 'Gustavo'
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos')

#Adicionando Input a um Dicionario[
#Adicionando um dicionário a uma lista sem conectar os dois usando copy

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Qual é seu estado?'))
    estado['sigla'] = str(input('Qual é a sigla do estado?'))
    brasil.append(estado.copy())

