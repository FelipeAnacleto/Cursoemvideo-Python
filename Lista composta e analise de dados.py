temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        mair = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print(f'Os dados foram {princ}')
print(f'ao todo, você cadastrou {len(princ)} Pessoas.')
print(f'O maior peso foi {mai}KG, peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print(f'O menor peso foi {men}KG')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
