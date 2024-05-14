# Crie um programa que encontre e mostre o segundo maior e o segundo menor números em uma lista de 10 números digitada pelo usuário.


numeros = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numeros_ordenados = sorted(numeros)

print("O segundo menor número é:", numeros_ordenados[1])

print("O segundo maior número é:", numeros_ordenados[-2])
