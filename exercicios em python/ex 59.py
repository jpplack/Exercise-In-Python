from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
r = ''

while r != '5':
    print('''O que você deseja fazer? 
              [1] Somar: 
              [2] Multiplicar
              [3] Maior
              [4] Novos números
              [5] Sair do programa''')

    r = str(input('>>>> Qual é a sua opção? ')).strip()

    if r == '1':
        s = n1 + n2
        print(f'A soma dos dois valores são: {s} ')

    elif r == '2':
        m = n1 * n2
        print(f'A multiplicação dos dois valores são: {m} ')

    elif r == '3':
        if n1 > n2:
            print(f'O {n1} é maior que o {n2}. ')
        elif n1 < n2:
            print(f'O {n2} é maior que {n1}. ')
        else: 
            print('Os dois valors são iguais! ')

    elif r == '4':
        print('Informe os valores novamente. ')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))

    elif r == '5':
        print('Finalizando... ')
        sleep(1)

    else:
        print('\033[31mOpção inválida! Tente novamente.\033[m')
    print('=-=' * 10)
    sleep(1)

print('Obrigado, por ter usado o programa! Volte logo!')