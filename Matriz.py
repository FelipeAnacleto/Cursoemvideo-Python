matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):  # colocar valores na lista matriz
    for c in range(0, 3):  # colocar valores na lista matriz
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):  # monstrar a matriz na tela
    for c in range(0, 3):  # monstrar a matriz na tela
        print(f'[{matriz[l][c]:^5}]', end='')  #  monstrar colunas f c centralizados '^' com 5 espaços
    print()  # sempre que termianr a coluna ele quebra pra fazer uma nova linha
