# Crie uma função que defina uma variável x dentro da função e imprima o valor de x na tela. Em seguida, fora da função, crie uma linha de código para imprimir o valor de x e analise o erro que será gerado ao tentar executar o programa.

def imprimir_x():
    x = 10
    print("O valor de x dentro da função é:", x)

imprimir_x()

try:
    print("O valor de x fora da função é:", x)
except NameError:
    print("A variável x não está definida fora da função.")

