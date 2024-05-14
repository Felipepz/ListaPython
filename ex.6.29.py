# Crie um generator que receba uma lista de números e retorne, a cada iteração, o quadrado do próximo número da lista. Use esse generator para imprimir os quadrados dos números de uma lista de 1 a 10.



def quadrado_proximo(lista):
    for num in lista:
        yield num ** 2

numeros = list(range(1, 11))

gerador = quadrado_proximo(numeros)

for quadrado in gerador:
    print(quadrado)

