from random import randint
from time import sleep
computador = randint(0, 10)
print('\033[1;35mSou seu computador.. Acabei de pensar em um número entre 0 e 10.\033[1;38m')
sleep(2)
print('será que você consegue adivinhar qual foi? ')
sleep(3)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[1;34mQual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[0;38mMais...')
        elif jogador > computador:
            print('\033[0;38mmenos')
print('\033[1;32mAcertou.\033[1;31mTentativas {}'.format(palpites))






