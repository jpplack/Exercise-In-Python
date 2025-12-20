print('\033[1;35m' + '='*40)
print(' PROGRAMA PARA EMPRESTIMO BANCARIO')
print('='*40 + '\033[m')

nome = str(input('Qual o nome completo: '))
sal = float(input(f'Qual o salário do Sr(a). {nome}: '))
casa = float(input('Qual o valor da casa que gostaria de financiar: '))
anos = int(input('Qual a quantidade de meses que gostaria de pagar: '))
prestacao = casa / anos
minimo = sal * 30 / 100

print('Para pagar umas casa de R${:.2f} em {} meses' .format(casa, anos), end='')
print(' a prestação será de R${:.2f}' .format(prestacao))

if prestacao <= minimo:
    print('Parabens! Seu emprestimo bancario foi aprovado!')
else:
    print('Infelizmente seu emprestimo foi negado!')
