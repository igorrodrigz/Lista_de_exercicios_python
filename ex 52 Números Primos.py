n = int(input('Digite um número : '))
tot = 0
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end= '')
    print(f'{c} ', end='')
print('\n\033[m O número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print(' E por isso ele é PRIMO!')
else:
    print(' E por isso ele NÂO é PRIMO!')
