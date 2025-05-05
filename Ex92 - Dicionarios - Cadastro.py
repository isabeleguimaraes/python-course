from datetime import date
import time
dados = {}

dados['nome'] = str(input('Qual o seu nome? '))
dados['ano'] = int(input('Qual o seu ano de nascimento?'))
dados['idade'] = date.today().year - dados['ano']
dados['ctps'] = int(input('Numero da sua carteira de trabalho (0 se não tiver)'))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano da sua contratação: '))
    dados['salario'] = int(input('Valor do salário mensal: '))
    ano_apos = dados['contratacao'] + 35
    dados['aposentadoria'] = ano_apos - dados['ano']
for k,v in dados.items():
    print(f'{k} = {v}')