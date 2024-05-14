# Crie um generator que produza uma sequência infinita de números inteiros, começando por 1. Em seguida, faça um laço para imprimir os primeiros 10 números dessa sequência.


def gerador_infinito():
    num = 1
    while True:
        yield num
        num += 1


sequencia = gerador_infinito()

for _ in range(10):
    print(next(sequencia))
