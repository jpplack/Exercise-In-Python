n1 = float(input('Qual a primeira nota do aluno: '))
n2 = float(input('Qual a segunda nota do aluno: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'O aluno teve a média {media}, consequentemente, foi aprovado!')
if media >= 5:
    print(f'O aluno teve a média {media}, portanto está de recuperação!')
else:
    print(f'O aluno teve a média {media}, portanto não foi aprovado!')
