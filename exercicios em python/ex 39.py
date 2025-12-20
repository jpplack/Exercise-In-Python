from datetime import date 

atual = date.today().year
nasc = int(input('Qual o ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('O cidadão deve se alistar neste ano letivo!')
elif idade < 18:
    print('O cidadão não atingiu a idade exigida. Ainda faltam {} anos para o alistamento obrigatório' .format(18 - idade))
else:
    print('O cidadão deveria ter se apresentado à {} anos atrás' .format(idade - 18))
