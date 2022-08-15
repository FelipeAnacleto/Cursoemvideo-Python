n1 = int(input('Primeiro valor'))
n2 = int(input('Segundo valor'))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>> Qual a sua opção'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('informe os números novamente:')
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa!')
