import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    
    while True:
        try:
            palpite = int(input("Adivinhe o número entre 1 e 10: "))
            
            if palpite < 1 or palpite > 10:
                raise ValueError("Por favor, insira um número entre 1 e 10.")
            
            if palpite == numero_secreto:
                print("Parabéns! Você acertou o número.")
                break
            else:
                print("Número errado. Tente novamente.")
        except ValueError:
            print("Por favor, insira apenas números inteiros entre 1 e 10.")

# Iniciando o jogo
jogo_adivinhacao()
