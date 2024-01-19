from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'O atleta tem {idade} anos. ')
if idade <= 9:
    print('Classificação Mirim.')
elif idade <= 14:
    print('Classificação Infantil.')
elif idade <= 19:
    print('Classificação Junior.')
elif idade <= 25:
    print('Classificação Sênior.')
else:
    print('Classificação Master.')