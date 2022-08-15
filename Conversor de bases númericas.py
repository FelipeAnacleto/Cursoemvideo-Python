num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção Inválida. Tente novamente.')
