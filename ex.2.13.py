# Crie um programa que verifique se um número inteiro digitado pelo usuário é divisível por outro número inteiro também digitado pelo usuário.


numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 % numero2 == 0:
    print(f"{numero1} é divisível por {numero2}.")
else:
    print(f"{numero1} não é divisível por {numero2}.")
