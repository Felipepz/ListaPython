def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def calcular():
    operacao = input("Escolha a operação (soma, subtração, multiplicação, divisão): ")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == "soma":
            resultado = soma(num1, num2)
        elif operacao == "subtração":
            resultado = subtracao(num1, num2)
        elif operacao == "multiplicação":
            resultado = multiplicacao(num1, num2)
        elif operacao == "divisão":
            resultado = divisao(num1, num2)
        else:
            raise ValueError("Operação inválida.")
        
        print("Resultado:", resultado)
    except ValueError as e:
        print("Erro:", e)

calcular()
