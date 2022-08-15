aluno = {}
aluno['Nome'] = str(input('Qual seu nome? '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'

elif 5 <= aluno['Média'] < 7:
    aluno['situação'] = 'Recuperação'

else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')