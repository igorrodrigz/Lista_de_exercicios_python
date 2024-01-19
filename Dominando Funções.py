def exibir_mensagem():
    print ('Olá mundo!')

def exibir_mensagem_2(nome):
    print(f'Olá {nome}, seja bem vindo ao mundo!')

def exibir_mensagem_3(nome = 'Anônimo'):
    print(f'Olá {nome}, seja bem vindo ao mundo!')

exibir_mensagem()
exibir_mensagem_2(nome='Igor')
exibir_mensagem_3()