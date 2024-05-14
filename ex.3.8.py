# Crie um programa que calcule e mostre o fatorial de um número digitado pelo usuário.

numero = int(input("Digite um número inteiro para calcular o fatorial: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print("O fatorial de", numero, "é:", fatorial)
