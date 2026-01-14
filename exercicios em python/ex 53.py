frase = str(input('Digite uma frase para verificarmos se é um palindromo: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')
