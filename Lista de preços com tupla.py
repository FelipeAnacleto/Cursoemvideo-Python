lista = ('shampoo', 2.50,
         'amaciante', 4.22,
         'sabonete', 7.50,
         'condicionador', 9.90,
         'h20', 10.00,
         'café', 3.55,
         'manteiga', 4.00,
         'peito de peru', 7.23,
         'queijo frescal', 8.00,
         'pão de queijo', 12.23,
         'coca cola', 15.33,)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS" :^40}')  # monstra o titulo centralizado.
print('-' * 40)

for pos in range(0, len(lista)):  # monstra a posição dos itens da lista começando na posicão 0 e indo ate a lista inteira.
    if pos % 2 == 0:  # monstra somente os produtos, pq eles estão em uma posição par.
                      # se o número estiver como 1 vai aparecer somente os preços .

        print(f'{lista[pos]:.<30}', end='')  # monstra cheio de ponto alinhados a esquerda .
    else:
        print(f'R${lista[pos]:>6.2f}')  # monstra os numeros alinhados a direita formatados em contabil, com duas casas decimais.
print('-' * 40)
