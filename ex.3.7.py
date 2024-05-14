# Crie um programa que leia vários números positivos digitados pelo usuário, até que ele digite um valor negativo. Ao fim, o programa deve mostrar a média dos números positivos digitados.

soma = 0
contador = 0

while True:
    numero = float(input("Digite um número positivo (ou negativo para encerrar): "))
    
    if numero < 0:
        break
    
    soma += numero
    contador += 1


if contador > 0:
    media = soma / contador
    print("A média dos números positivos digitados é:", media)
else:
    print("Nenhum número positivo foi digitado.")
