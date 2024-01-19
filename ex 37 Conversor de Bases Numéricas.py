num = int(input('Digite um número inteiro: '))
base = int(input('''escolha a base para conversão
[1] converter para binário
[2] converter para octal
[3] converter hexadecimal'''))
if base == 1:
    print(f'{num} convertido para binario é igual a {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else :
    print('Digite um número valído.')
