from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    n = int(input(f'Em que ano a {c} pessoa nasceu: '))
    idade = atual - n
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Teveram {totmenor} pessoas cadastradas menores de idade e {totmaior} pessoas cadastradas maiores de idade.')
