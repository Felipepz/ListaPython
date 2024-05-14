# Crie um programa que pergunte ao usuário seu salário e exiba uma mensagem de "Alto salário" se o salário for maior do que R$10.000,00, ou "Baixo salário" caso contrário.

salario = float(input("Digite o seu salário: R$"))

if salario > 10000:
    print("Alto salário")
else:
    print("Baixo salário")
