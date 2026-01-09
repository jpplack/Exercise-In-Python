n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = n1 + (10 - 1) * razao
for c in range(n1, decimo + razao, razao):
    print('{} '.format(c), end='> ')
print('Acabou!')