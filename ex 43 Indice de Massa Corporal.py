peso = float(input('Qual é o seu peso? (kg) : '))
altura = float(input('Qual é sua altura? (m) : '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc}')
if imc <= 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc  < 25 :
    print('Peso Ideal')
elif 25 <= imc < 30 :
    print('Sobrepeso')
elif 30 <= imc < 40 :
    print('Obesidade')
elif imc >= 40 :
    print('Obesidade Morbida')