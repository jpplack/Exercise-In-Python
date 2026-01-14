from random import randint
computador = randint(0, 10)
print('Sou seu computador. . .')
print('Entre 0 e 10, será que você consegue adivinhar o numero que estou pensando?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais...')
        elif jogador > computador:
            print('Um pouco menos...')
print(f'Acertou! O jogador acertou em {palpite} palpite(s).')