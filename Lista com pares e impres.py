núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('digite um valor: '))
    if valor % 2 == 0:  # verificar se os valores sao pares
        núm[0].append(valor)
    else:
        núm[1].append(valor)

núm[0].sort()  # monstrar os numeros pares em ordem
núm[1].sort()  # monstrar os numeros imapares em ordem
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores impares digitados foram: {núm[1]}')
