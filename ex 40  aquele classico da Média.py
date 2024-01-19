nota1 = int(input('Qual a nota da sua primeira prova : '))
nota2 = int(input('Qual a nota da sua segunda prova : '))
media = (nota2 + nota1) / 2
if media >= 5.0 :
    print('Que pena, você foi reprovado ! ')
elif media >=5 and media < 7 :
    print('Você foi aprovado, mas foi por pouco. Você esta de recuperação !')
else :
    print('Parabéns você aprovado com satisfação ! ')