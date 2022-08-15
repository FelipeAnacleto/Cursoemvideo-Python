frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = junto[::-1] funciona também sem usar o laço de repetição
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')