lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche))  # monstra a lista em ordem.
print(lanche)  # a Tupla não se altera, apenas se ordena.
print('-> ' * 30)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(f'a minha mãe comeu {lanche[:1]} ela é uma gulosa')
print(c.index(8))  # Monstra em que posição esta o número que esta no objeto da tupla.
print(c.count(5))  # faz a conta de quantas vezes o número que esta no objeto da tupla aparece.

