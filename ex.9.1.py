while True:
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
        break  
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
    except ZeroDivisionError:
        print("Erro: divisão por zero. Por favor, tente novamente.")
