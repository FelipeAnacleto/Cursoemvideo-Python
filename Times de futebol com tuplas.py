times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atletico-GO')

print(f'Lista de times do brasileirão: {times}')

print('_' * 100)
print(f'Os 5 Primeiros são: {times[0:5]}')
print('_' * 100)
print(f'Os 4 últimos são: {times[-5:]}')
print('_' * 100)
print(f'Times em ordem alfabética: {sorted(times)}')
print('_' * 100)
print(f'O chapecoense está na {times.index("Chapecoense")} position')