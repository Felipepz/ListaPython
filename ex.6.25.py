# Desenvolva um programa que simule um sorteio de nomes para um amigo secreto. Cada pessoa só pode tirar outra pessoa uma vez e uma pessoa não pode tirar a si mesma. O programa deve continuar sorteando até que todas as pessoas tenham tirado um amigo secreto. Utilize a função random.choice para realizar o sorteio. As pessoas participantes são: "Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana". Ao final, o programa deve exibir quem tirou quem no amigo secreto.


import random

pessoas = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana"]
sorteio = {}
amigo_secreto = list(pessoas)

for pessoa in pessoas:
    amigo_secreto.remove(pessoa)
    amigo = random.choice(amigo_secreto)
    sorteio[pessoa] = amigo
    amigo_secreto.append(pessoa)

print("Resultado do sorteio do amigo secreto:")
for pessoa, amigo in sorteio.items():
    print(f"{pessoa} tirou {amigo}")
