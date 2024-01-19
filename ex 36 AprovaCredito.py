print('Seja bem vindo A Central de Crédito do Consumir do Mr.Robot Bank !')
valorcasa = float(input('Por favor, digite o valor da casa : '))
salario = float(input('Digite sua Renda Média mensal : '))
prazo = int(input('Em Quantos anos deseja quitar o financiamento : '))
import time
print('Processando... !')
time.sleep(2)
prestacao = prazo * 12 / valorcasa
minimo = (salario * 30) / 100
if prestacao < minimo :
    print('Seu crédito Imobiliario foi aprovado, PARABENS !')
else :
    print('Seu crédito Imobiliario foi recusado, INFELIZMENTE VOCÊ É POBRE !')

