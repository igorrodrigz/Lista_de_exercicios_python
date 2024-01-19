print(20*'-=')
print('     BEM VINDO A LOJA MR.ROBOT !')
valor = float(input('Qual o valor total da compra?'))

forma = float(input('''Insira a forma de pagamento?

[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros'''))

if forma == 1 :
    desconto = valor * 10 / 100
    valortotal = valor - desconto
    print(f'Você recebeu um desconto de R${desconto:.2f} o valor total de sua compra será R${valortotal:.2f}')
elif forma == 2 :
    desconto = valor * 5 / 100
    valortotal = valor - desconto
    print(f'Você recebeu um desconto de R${desconto:.2f} o valor total de sua compra será R${valortotal:.2f}')
elif forma == 3 :
    print(f'O valor total de sua compra será R${valor:.2f}')
elif forma == 4 :
    juros = valor * 20 / 100
    valortotal = valor + juros
    print(f'O valor total de sua compra será R${valortotal:.2f}')
else :
    print('Digite um número valido.')
print('OBRIGADO POR COMPRAR COM O MR.ROBOT, VOLTE SEMPRE !')
print(20*'-=')

