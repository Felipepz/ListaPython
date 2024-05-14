import time

def exibir_data_hora():
    data_hora_atual = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("Data e hora atuais:", data_hora_atual)

exibir_data_hora()