from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(20*'-=')
#print(f'O computador escolheu {itens[computador]}')
print(20*'-=')
print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura''')
print(20*'-=')
jogador = int(input('Qual é a sua jogada?'))
from time import sleep
sleep(1)
print('PEDRA...')
sleep(1)
print('PAPEL... OU...')
sleep(1)
print('TESOURA... !')
sleep(1)
print(f'o Jogador jogou {itens[jogador]}')
print(f'O computador escolheu {itens[computador]}')
if computador == 0:
    if jogador == 0:
        print('JOGO EMPATOU! JOGUE NOVAMENTE')
    elif jogador == 1:
        print('O JOGADOR VENCEU, PARABÉNS !')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU !')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('JOGO EMPATOU, JOGUE NOVAMENTE !')
    elif jogador == 2:
        print('jOGADOR VENCEU, PARABÉNS')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU, PARABÉNS !')
    elif jogador == 1:
        print('COMPUTADOR VENCEU !')
    elif jogador == 2:
        print('JOGO EMPATOU, JOGUE NOVAMENTE !')
