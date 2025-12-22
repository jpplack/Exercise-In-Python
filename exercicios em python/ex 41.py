from datetime import date
nome = input('Qual o nome completo do atleta: ')
nasc = int(input('Qual o ano de nascimento do atleta:'))
atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print(f'A categoria do atleta {nome} é MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'A categoria do Atleta {nome} é INFANTIL.')
elif idade > 14 and idade <=19:
    print(f'A categoria do atleta {nome} é JUNIOR.')
elif idade > 19 and idade <=25:
    print(f'A categoria do atleta {nome} é ELITE.')
else:
    print(f'A categoria do atleta {nome} é MASTER.')