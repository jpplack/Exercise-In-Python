sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()

while sexo not in 'MF' or sexo == '':
    print('\033[31mERRO! Por favor, digite uma resposta válida [M/F]. \033[m')
    sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()

print(f'Sexo {sexo} registrado com sucesso! 🚀')