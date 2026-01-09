print('\033[1;35m' + '='*40)
print('MOSTRANDO NUMEROS PARES!') 
print('='*40 + '\033[m')

print ('Esses são todos os numeros pares entre 0 e 50: ')

for c in range(0, 51, 2):
    print (c, end=' ')