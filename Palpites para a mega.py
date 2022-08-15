from random import randint
lista = list()
jogos = list()
quant = int(input('quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:  # verificar se numero não esta na lista
            lista.append(num)  # acrescentar numero na lista
            cont += 1  # contador recebe + 1
        if cont >= 6:  # se o contador for maior ou igual a 5
            break  # intemrrompe o laço infinito
    lista.sort()  # coloca os numeros em ordem
    jogos.append(lista[:])  # criar uma cópia da lista
    lista.clear()
    tot += 1
for i, l, in enumerate(jogos):
    print(f'jogo {i+1}: {l}')

