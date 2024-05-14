# Crie um programa que verifique se um número digitado pelo usuário é primo.



numero = int(input("Digite um número inteiro: "))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, "não é um número primo.")
            break
    else:
        print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
