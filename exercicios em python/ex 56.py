mediaidade = 0
somaidade = 0
velho = 0
mulher = 0
for p in range(1, 5):
    print(f'----{p}ª PESSOA----')
    str(input('Nome: '))

    idade = int(input('Idade: '))
    somaidade += idade 

    s = str(input('Sexo [M/F]: ')).upper()
    if s == 'M' and p == 1:
        velho = idade
    if s == 'F':
        if idade < 20:
            mulher += 1      
    else:
        if idade > velho:
            velho = idade
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade}.')
print(f'O homem mais velho tem {velho}.')
print(f'Ao todo são {mulher} com menos de 20 anos.')
