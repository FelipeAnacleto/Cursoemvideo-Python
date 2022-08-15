nomes = [5, 10, 3, 8, 10,]  # lista são mutaveis em python
nomes[2] = 7  # numero 2 passa a ser sete na lista
nomes.append(9)  # adicionando o valor nove a lista
nomes.sort()  # coloca a lista em ordem
nomes.sort(reverse=False)  # coloca a lista em ordem de trás pra frente
nomes.insert(2, 0)  # na posição 2 inserir o valor zero
nomes.pop()  # apaga o ultimo elemento da lista se não colocar nada, ou oque voce colocar no parenteses ele apaga
nomes.remove(10)  # apaga o primeiro elemento da lista que voce mandou eliminar
if 4 in nomes:  # procura na lista se tem o numero 4
    nomes.remove(4)  # se tiver o numero 4 na lista ele vai remover o primeiro elemento
else:
    print(f'não achei nenhum numero quatro')

print(nomes)
print(f'Essa lista em {len(nomes)} elementos')  # conta quantos items tem na lista

