pac = input('Qual o nome completo do paciente: ')
peso = float(input('Qual o peso do paciente em KG: '))
alt = float(input('Qual a altura do paciente em M: '))
imc = peso / (alt * alt)

if imc < 18.5: 
    print(f'O paciente {pac} está com o IMC em {imc:.2f}, portanto está ABAIXO DO PESO.')
elif imc > 18.5 and imc <= 25:
    print(f'O paciente {pac} está com o IMC em {imc:.2f}, portanto está no PESO IDEAL.')
elif imc > 25 and imc <= 30:
    print(f'O paciente {pac} está com o IMC em {imc:.2f}, portanto está em SOBREPESO.')
elif imc > 30 and imc <= 40:
    print(f'O paciente {pac} está com o IMC em {imc:.2f}, portanto está no estado de OBESIDADE.')
else:
     print(f'O paciente {pac} está com o IMC em {imc:.2f}, portanto está no estado de OBESIDADE MORBIDA.')
