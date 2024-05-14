# Crie uma função que tenha um número inteiro como parâmetro e retorne True se o número for par e False se o número for ímpar. Em seguida, crie uma chamada para essa função passando argumentos para os parâmetros e mostrando o resultado na tela.


def verificar_paridade(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = 5
resultado = verificar_paridade(numero)
print(f"O número {numero} é par? {resultado}")
