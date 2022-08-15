from datetime import datetime

dados = {}
dados['nome'] = str(input('Qual seu nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}  ')
