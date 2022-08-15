from random import randint
from time import sleep

computador = randint(0, 5)  # faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei'))  # O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! você conseguiu me vencer!')
else:
    print('Ganhei! eu pensei no número {} e não no {}!'.format(computador, jogador))
