print('\033[1;35m' + '='*40)
print(' LOJA DO SINFOROSO')
print('='*40 + '\033[m')

preco = float(input('Qual o valor total da compra: R$'))
print('''Escolha uma opção de pagamento:
[ 1 ] À vista dinheiro/ cheque
[ 2 ] À vista no catão
[ 3 ] 2x no catão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual seria a forma de pagamento? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2 
    print(f'O valor da sua parcela será de R${parcela}')
elif opcao == 4:
    num = int(input('Qual a quantidade de parcelas: '))
    total = preco + (preco * 20 / 100)
    parcela = total / num
    print(f'O valor da sua parcela será de R${parcela}')
print(f'Sua compra de R${preco} ficara no valor total de R${total}.')

