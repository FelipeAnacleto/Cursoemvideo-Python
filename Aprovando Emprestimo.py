casa = float(input('Valor da Casa: R$'))
salário = float(input('Salário do comprador'))
anos = int(input('Quantos anos de financiamento'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar a casa de R${:.2f} em {} Anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('\033[1;32mO empréstimo pode ser CONCEDIDO')
else:
    print('\033[1;31mEmpréstimo NEGADO!')
