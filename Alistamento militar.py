from datetime import date
atual = date.today().year
str(input('''Gênero :'
[ 1 ] MASCULINO
[ 2 ] FEMININO'''))
opção = str(input('  ')).strip()
if opção == '2':
    print('\033[1:31mVocê nao precisa se alistar')
    exit()
else:
    print('\033[1:32mSegue abaixo as instruções de alistamento: ')
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
