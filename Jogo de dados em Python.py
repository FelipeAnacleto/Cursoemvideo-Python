from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),  # dicionarios com os jogadores e a função random.
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = {}

print('Valores sorteados:')
for k, v in jogo.items():  # Monstrar as keys que são os jogadores, e values que são os valores do dicionario.
    print(f'{k} tirou {v} no dado')  # Monstrar os jogadores e os valores
    sleep(1)  # exibir com intervalo de 1 seg

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('_=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} ')
    sleep(1)
