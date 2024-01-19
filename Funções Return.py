def calcula_total(numeros):
    return sum(numeros)

print(calcula_total([10, 10, 10]))

def calculo_numeros(algoritmos):
    return max(algoritmos)

print (calculo_numeros([10, 20, 30, 40]))

def antecessor_sucessor_numerico(numericos):
    antecessor = numericos - 1
    sucessor = numericos + 1
    return antecessor, sucessor

print(antecessor_sucessor_numerico(50))