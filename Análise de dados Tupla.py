num = (int(input('Digite um número ')),
       int(input('Digite outro número ')),
       int(input('Digite mais um numero ')),
       int(input('Digite o ultimo numero ')))
print(f'Você digitou os valores {num}')
print(f'o Valor 9 apareceu {num.count(9)} vezes')  # conta quantas vezes o numero pedido aparece
if 3 in num:  # Verificar so o numero 3 esta na tupla
    print(f'o Valor 3 apareceu na {num.index(3)} Posição')  # em que lugar o numero pedido apareceu pela primeira vez
else:
    print(f'o numero 3 nao foi digitado')  # corrige o erro caso pessoa não digite o numero 3
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')
