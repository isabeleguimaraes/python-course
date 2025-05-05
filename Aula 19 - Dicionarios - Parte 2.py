#Criando um dicionário dentro de outro.
#O Dicionário com o nome dos alunos, contem o dicionario de notas de alunos.
students = {
    'Sajjad': {'Math': 100, 'English': 95},
    'David': {'Math': 95, 'English': 100}
}

#Para eu indicar um valor específico do dicionário, eu preciso especificar qual dicionário, qual key(aluno) e
# qual key do dicionário de dentro.

print(students['Sajjad']['English']) # Isso vai corresponder a 95

#Para substituir um valor, devo apenas nomeá-lo.

students['Sajjad']['English'] = 100 #Isso irá alterar o valor do item

#Para adicionar uma nova key (aluno) nesse dicionário, e guardar um valor, posso definir assim:
'''students['Alex'] = 85'''

#Porém, para adicionar um dicionário dentro de Alex, eu preciso definir que é um dicionário, não apenas um valor solto.

students['Alex'] = {'Math': 80, 'English': 90}
#ou
students['Amanda'] = {} #crio um dicionario dentro da key Amanda
students['Amanda']['Math'] =  85 #crio o valor 85 dentro da key Math que está na key Amanda

#Methods

students.keys() #Ve as Keys do dicionario
students.values() #Ve os Values do dicionario
students.clear() #Limpa os dados do dicionario
students.get('Sajjad') #Vai pegar os Values da Key #Nao vai dar erro se nao existir
students.pop('Sajjad') #Remove o value correspondente a key



print(students)
