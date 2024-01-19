from datetime import date
atual = date.today().year
anonasc = int(input('Ano de Nascimento : '))
idade = atual - anonasc
saldo = idade - 18
print(f'Quem nasceu em {anonasc} tem {idade} em {atual}. ')
if idade == 18 :
    print('Você precisa se apresentar á Junta do Serviço Militar para alistamento IMEDIATAMENTE !')
elif idade < 18 :
    print('Você ainda não precisa se Alistar ao Serviço Militar Obrigatório ! ufa... ')
    print(f'Ainda faltam {saldo}')
elif idade > 18 :
    ano = atual - saldo
    print(f'Olá Mr, Robot. Você já deveria ter se alistado em {ano}')